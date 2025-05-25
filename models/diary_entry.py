from __future__ import annotations

from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import xlsxwriter
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Polygon

from utils.exceptions.heatmap_export_failed import HeatmapExportFailed
from utils.exceptions.xlsx_export_failed import XlsxExportFailed
from utils.i18n import Translator


class DiaryEntry:
    labels_number_mapping = {
        "negative_sentiment": -1,
        "neutral_sentiment": 0,
        "positive_sentiment": 1,
    }

    labels_color_maping = {
        'positive_sentiment': '#4CAF50',
        'neutral_sentiment': '#2196F3',
        'negative_sentiment': '#F44336',
        'default': '#DDDDDD'
    }

    days = [Translator.translate('Heatmap.Monday'),
            Translator.translate('Heatmap.Tuesday'),
            Translator.translate('Heatmap.Wednesday'),
            Translator.translate('Heatmap.Thursday'),
            Translator.translate('Heatmap.Friday'),
            Translator.translate('Heatmap.Saturday'),
            Translator.translate('Heatmap.Sunday')]

    month_names = [Translator.translate('Heatmap.January'),
                   Translator.translate('Heatmap.February'),
                   Translator.translate('Heatmap.March'),
                   Translator.translate('Heatmap.April'),
                   Translator.translate('Heatmap.May'),
                   Translator.translate('Heatmap.June'),
                   Translator.translate('Heatmap.July'),
                   Translator.translate('Heatmap.August'),
                   Translator.translate('Heatmap.September'),
                   Translator.translate('Heatmap.October'),
                   Translator.translate('Heatmap.November'),
                   Translator.translate('Heatmap.December')]

    weeks = [1, 2, 3, 4, 5, 6]

    def __init__(self, db_object: dict):
        self.id = db_object.get("id")
        self.entry_text = db_object.get("entry_text")
        creation_date = db_object.get("creation_date")
        if creation_date:
            self.creation_date = datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S")
        self.sentiment = db_object.get("sentiment")
        self.user_id = db_object.get("user_id")

    @staticmethod
    def export_list_to_xls(data: list[DiaryEntry], file_path, hide_content=False):
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            workbook = xlsxwriter.Workbook(file_path)
            worksheet = workbook.add_worksheet()
            column_names = [Translator.translate('Entry.Content'),
                            Translator.translate('Entry.Sentiment'),
                            Translator.translate('Entry.Date')]

            for i in range(len(column_names)):
                worksheet.write(0, i, column_names[i])

            for i, obj in enumerate(data):
                if not hide_content:
                    worksheet.write(i + 1, 0, obj.entry_text)
                worksheet.write(i + 1, 1, obj.creation_date.strftime("%Y-%m-%d %H:%M") if obj.creation_date else "")
                worksheet.write(i + 1, 2, obj.sentiment)

            worksheet.autofit()
            workbook.close()
        except Exception:
            raise XlsxExportFailed()

    @staticmethod
    def export_list_to_heatmap(data: list[DiaryEntry], start_time: datetime, end_time: datetime, file_path: str):
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            data.sort(key=DiaryEntry.diary_entry_date)
            date_entry_dict = {}
            for j in data:
                if date_entry_dict.get(j.creation_date.date()) is None:
                    date_entry_dict[j.creation_date.date()] = []
                date_entry_dict[j.creation_date.date()].append(j)
            date_sentiment_dict = {}
            for key, value in date_entry_dict.items():
                if len(value) == 1:
                    date_sentiment_dict[key] = value[0].sentiment
                else:
                    date_sentiment_dict[key] = DiaryEntry._count_sentiment4list(value)
            return DiaryEntry._generate_sentiment_calendar(date_sentiment_dict, start_time, end_time,
                                                           output_file=file_path)
        except Exception as e:
            print(e)
            raise HeatmapExportFailed()

    @staticmethod
    def _count_sentiment4list(data: list[DiaryEntry]) -> str:
        sentiment = 0
        for entry in data:
            sentiment += DiaryEntry.labels_number_mapping.get(entry.sentiment, 0)
        sentiment /= len(data)
        if sentiment < -0.20:
            return "negative_sentiment"
        elif sentiment > 0.20:
            return "positive_sentiment"
        return "neutral_sentiment"

    @staticmethod
    def diary_entry_date(element: DiaryEntry):
        return element.creation_date.date()

    @staticmethod
    def _generate_sentiment_calendar(date_sentiment_dict, start_time, end_time, output_file='sentiment_calendar.png'):
        if isinstance(start_time, str):
            start_time = datetime.strptime(start_time, '%Y-%m-%d')
        if isinstance(end_time, str):
            end_time = datetime.strptime(end_time, '%Y-%m-%d')

        sentiment_series = DiaryEntry._generate_sentiment_data(date_sentiment_dict, start_time, end_time)

        files = []

        for year in range(start_time.year, end_time.year + 1):
            day_nums, day_sentiments = DiaryEntry._split_months(sentiment_series, year)
            current_year_file = f"{output_file.split('.')[0]}_{year}.png"
            DiaryEntry._create_sentiment_calendar(day_nums, day_sentiments, year, current_year_file)
            files.append(current_year_file)
        return files

    @staticmethod
    def _generate_sentiment_data(date_sentiment_dict: dict, start_time: datetime, end_time: datetime):
        idx = pd.date_range(start_time, end_time, freq='D')
        sentiment_series = pd.Series(index=idx, dtype=object)

        for date, sentiment in date_sentiment_dict.items():
            if isinstance(date, str):
                date = datetime.strptime(date, '%Y-%m-%d').date()
            date = pd.Timestamp(date)
            if date in sentiment_series.index:
                sentiment_series[date] = sentiment  # Don't convert to lowercase here

        return sentiment_series

    @staticmethod
    def _split_months(sentiment_series, year):
        df = sentiment_series[sentiment_series.index.year == year]

        empty_matrix = np.empty((6, 7), dtype=object)
        empty_matrix[:] = None

        day_nums = {m: np.empty((6, 7)) for m in range(1, 13)}
        day_sentiments = {m: np.copy(empty_matrix) for m in range(1, 13)}

        for m in day_nums:
            day_nums[m][:] = np.nan

        row = 0

        for date, sentiment in df.items():

            day = date.day
            month = date.month
            col = date.dayofweek

            if date.is_month_start:
                row = 0

            day_nums[month][row, col] = day
            day_sentiments[month][row, col] = sentiment

            if col == 6:
                row += 1

        return day_nums, day_sentiments

    @staticmethod
    def _create_sentiment_calendar(day_nums, day_sentiments, year, output_file):
        fig, ax = plt.subplots(3, 4, figsize=(14.85, 10.5))

        cmap = ListedColormap([DiaryEntry.labels_color_maping['positive_sentiment'],
                               DiaryEntry.labels_color_maping['neutral_sentiment'],
                               DiaryEntry.labels_color_maping['negative_sentiment']])

        for i, axs in enumerate(ax.flat):
            month_num = i + 1

            sentiment_matrix = np.zeros_like(day_nums[month_num], dtype=float)
            for w in range(6):
                for d in range(7):
                    sentiment = day_sentiments[month_num][w, d]
                    if sentiment == 'positive_sentiment':
                        sentiment_matrix[w, d] = 0
                    elif sentiment == 'neutral_sentiment':
                        sentiment_matrix[w, d] = 1
                    elif sentiment == 'negative_sentiment':
                        sentiment_matrix[w, d] = 2
                    else:
                        sentiment_matrix[w, d] = np.nan

            axs.imshow(sentiment_matrix, cmap=cmap, vmin=0, vmax=2)
            axs.set_title(DiaryEntry.month_names[i])

            axs.set_xticks(np.arange(len(DiaryEntry.days)))
            axs.set_xticklabels(DiaryEntry.days, fontsize=10, fontweight='bold', color='#555555')
            axs.set_yticklabels([])

            axs.tick_params(axis='both', which='both', length=0)
            axs.xaxis.tick_top()

            axs.set_xticks(np.arange(-.5, 6, 1), minor=True)
            axs.set_yticks(np.arange(-.5, 5, 1), minor=True)
            axs.grid(which='minor', color='w', linestyle='-', linewidth=2.1)

            for edge in ['left', 'right', 'bottom', 'top']:
                axs.spines[edge].set_color('#FFFFFF')

            for w in range(len(DiaryEntry.weeks)):
                for d in range(len(DiaryEntry.days)):
                    day_num = day_nums[month_num][w, d]
                    sentiment = day_sentiments[month_num][w, d]

                    if not np.isnan(day_num):
                        axs.text(d + 0.45, w - 0.31, f"{int(day_num)}",
                                 ha="right", va="center",
                                 fontsize=6, color="#003333", alpha=0.8)

                    patch_coords = ((d - 0.1, w - 0.5),
                                    (d + 0.5, w - 0.5),
                                    (d + 0.5, w + 0.1))
                    triangle = Polygon(patch_coords, fc='w', alpha=0.7)
                    axs.add_artist(triangle)

                    if sentiment is None and not np.isnan(day_num):
                        patch_coords = ((d - 0.5, w - 0.5),
                                        (d - 0.5, w + 0.5),
                                        (d + 0.5, w + 0.5),
                                        (d + 0.5, w - 0.5))
                        square = Polygon(patch_coords, fc=DiaryEntry.labels_color_maping['default'])
                        axs.add_artist(square)

        fig.suptitle(Translator.translate('Heatmap.SentimentCalendar').format(year=year), fontsize=16)
        plt.subplots_adjust(left=0.04, right=0.96, top=0.82, bottom=0.04)

        legend_elements = [
            plt.Rectangle((0, 0), 1, 1, fc=DiaryEntry.labels_color_maping['positive_sentiment']),
            plt.Rectangle((0, 0), 1, 1, fc=DiaryEntry.labels_color_maping['neutral_sentiment']),
            plt.Rectangle((0, 0), 1, 1, fc=DiaryEntry.labels_color_maping['negative_sentiment']),
            plt.Rectangle((0, 0), 1, 1, fc=DiaryEntry.labels_color_maping['default'])
        ]
        fig.legend(
            legend_elements,
            [Translator.translate('Heatmap.Positive'),
             Translator.translate('Heatmap.Neutral'),
             Translator.translate('Heatmap.Negative'),
             Translator.translate('Heatmap.NoData')],
            loc='upper right',
            bbox_to_anchor=(1.0, 1.0),
            bbox_transform=fig.transFigure
        )

        plt.savefig(output_file, dpi=300)
        plt.close()
