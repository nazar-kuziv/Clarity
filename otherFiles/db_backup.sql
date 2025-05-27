--
-- PostgreSQL database dump
--

-- Dumped from database version 15.8
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA IF NOT EXISTS public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_table_access_method = heap;

--
-- Name: diaries_entries; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.diaries_entries (
    id integer NOT NULL,
    entry_text text NOT NULL,
    creation_date timestamp without time zone NOT NULL,
    sentiment text NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.diaries_entries OWNER TO postgres;

--
-- Name: diaries_entries_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.diaries_entries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.diaries_entries_id_seq OWNER TO postgres;

--
-- Name: diaries_entries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.diaries_entries_id_seq OWNED BY public.diaries_entries.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email text NOT NULL,
    password text NOT NULL,
    name text NOT NULL,
    last_name text NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: diaries_entries id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diaries_entries ALTER COLUMN id SET DEFAULT nextval('public.diaries_entries_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: diaries_entries; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.diaries_entries (id, entry_text, creation_date, sentiment, user_id) FROM stdin;
28	Dziś spędziłem cały dzień w biurze. Mimo że było dość monotonnie, udało mi się zrobić wszystkie zadania. Czułem się neutralnie, bo dzień minął dość zwyczajnie.	2025-01-23 08:15:00	positive_sentiment	1
31	Dzień minął bardzo spokojnie. Spędziłem go na porządkowaniu rzeczy w domu. Czułem się zrelaksowany, ale trochę samotny.	2025-01-20 19:30:00	positive_sentiment	1
37	Dziś był stresujący dzień. Miałem kilka pilnych spraw w pracy, które wymagały natychmiastowej uwagi. Po zakończeniu pracy poczułem ulgę, ale i zmęczenie.	2025-01-14 19:15:00	positive_sentiment	1
6	Dziś odwiedziłem rodzinę. Rozmawialiśmy i jedliśmy pyszny obiad. Czuję się wdzięczny za te chwile i cieszę się bliskością bliskich.	2025-01-06 14:20:00	negative_sentiment	1
1	Dziś spędziłem dzień na spacerze w parku. Było słonecznie, a świeże powietrze poprawiło mi nastrój. Czuję się spokojniejszy i szczęśliwszy.	2025-01-01 10:30:00	positive_sentiment	1
8	Dzień spędzony w bibliotece. Przeczytałem kilka ciekawych artykułów. Byłem skupiony i zadowolony z siebie, czuję się spełniony.	2025-01-08 13:30:00	positive_sentiment	1
50	Rano miałem trudności w pracy, ale później udało mi się rozwiązać problem. Czułem się zrelaksowany, ale trochę sfrustrowany początkiem dnia.	2025-01-01 08:30:00	positive_sentiment	1
60	Rano było trochę chaotycznie, ale później w pracy wszystko się uspokoiło. Czułem się trochę zestresowany, ale pod koniec dnia byłem zadowolony z tego, co osiągnąłem.	2024-12-22 16:00:00	positive_sentiment	1
63	Dziś spędziłem czas sam. Zrobiłem porządek w mieszkaniu, poczytałem książkę i odpocząłem. Czułem się zrelaksowany, ale trochę samotny.	2024-12-19 14:30:00	positive_sentiment	1
70	Dzień był dość monotonny. Praca poszła gładko, ale nie było żadnych szczególnych wydarzeń. Czułem się spokojnie, ale trochę nudziłem się w pracy.	2024-12-12 17:30:00	positive_sentiment	1
42	Dziś miałem sporo pracy, ale nie było to nic nadzwyczajnego. Czułem się dość neutralnie przez cały dzień, bez większych wzlotów ani upadków.	2025-01-09 08:30:00	neutral_sentiment	1
39	Dziś był bardziej leniwy dzień. Spędziłem czas w domu, odpoczywając i oglądając filmy. Czułem się spokojnie i zrelaksowany, ale brakowało mi trochę energii.	2025-01-12 14:00:00	neutral_sentiment	1
58	Dziś byłem trochę przytłoczony obowiązkami. Miałem dużo rzeczy do zrobienia w pracy, ale udało mi się wszystko załatwić. Czułem się zmęczony, ale dumny z efektów.	2024-12-24 17:30:00	neutral_sentiment	1
69	Dziś miałem trudny dzień. W pracy pojawiły się komplikacje, które opóźniły wszystkie moje zadania. Czułem się sfrustrowany, ale na koniec dnia wszystko się wyjaśniło.	2024-12-13 20:00:00	neutral_sentiment	1
74	Dziś był trudny dzień, ponieważ miałem dużo rzeczy do załatwienia w pracy. Czułem się trochę przytłoczony, ale wieczorem udało mi się zrelaksować przy filmie.	2024-12-08 20:30:00	neutral_sentiment	1
2	Poranek zaczął się od pysznej kawy. Pracowałem nad projektem, a potem zrelaksowałem się oglądając film. Czuję się produktywnie i zadowolony.	2025-01-02 09:45:00	neutral_sentiment	1
40	Dziś miałem trudności w pracy. Miałem poczucie, że nie wszystko idzie zgodnie z planem, ale później udało mi się poprawić sytuację. Czułem się zadowolony, ale zmęczony.	2025-01-11 17:30:00	negative_sentiment	1
3	Dziś cały dzień padał deszcz. Siedziałem w domu, czytałem książki i słuchałem muzyki. Pomimo pogody czułem spokój i zadowolenie.	2025-01-03 12:00:00	positive_sentiment	1
78	Dziś spędziłem czas sam w domu. Zrobiłem porządek, poczytałem książkę i odpocząłem. Czułem się zrelaksowany, ale trochę samotny.	2024-12-04 17:30:00	positive_sentiment	1
85	Dziś miałem dość monotonny dzień w pracy. Nie było żadnych ekscytujących wydarzeń, ale udało mi się zrealizować wszystkie zadania. Czułem się spokojnie, ale trochę znudzony.	2024-11-27 18:00:00	positive_sentiment	1
86	Rano wstałem pełen energii, ale potem w pracy miałem sporo do zrobienia. Czułem się trochę przytłoczony, ale wieczorem udało mi się odpocząć.	2024-11-26 19:30:00	positive_sentiment	1
89	Dziś miałem spokojny dzień, spędzony głównie na pracy w domu. Czułem się zrelaksowany, choć trochę samotny. Wieczorem poczułem się lepiej po spędzeniu czasu z książką.	2024-11-23 17:00:00	positive_sentiment	1
96	Dziś spędziłem spokojny dzień w domu. Wykonałem kilka drobnych prac domowych i poczytałem książkę. Czułem się zrelaksowany, ale trochę samotny.	2024-11-16 16:00:00	positive_sentiment	1
24	Wieczorem obejrzałem ciekawy dokument o naturze. Zainspirowało mnie to do planowania wycieczki w góry. Czuję się zmotywowany do działania.	2025-01-24 20:30:00	positive_sentiment	1
109	Dziś był bardzo relaksujący dzień. Wspólnie z przyjaciółmi oglądaliśmy filmy i rozmawialiśmy. Czuję się zadowolony, że spędziłem czas z bliskimi.	2025-01-22 18:00:00	positive_sentiment	1
105	Dziś rano poszedłem na jogę. To była świetna rozgrzewka i pozwoliła mi poczuć się pełnym energii. Dzień rozpoczął się naprawdę dobrze.	2025-01-26 07:30:00	positive_sentiment	1
95	Dziś miałem dzień pełen wyzwań. W pracy było trochę problemów, które wymagały szybkich rozwiązań. Czułem się trochę zestresowany, ale udało mi się wszystko ogarnąć.	2024-11-17 18:30:00	neutral_sentiment	1
44	Rano miałem ciężką decyzję do podjęcia, co trochę mnie stresowało. Na szczęście po kilku godzinach wszystko się wyjaśniło i poczułem się spokojniej.	2025-01-07 15:00:00	negative_sentiment	1
30	Rano miałem ciężki dzień, bo znowu nie mogłem się obudzić na czas. W pracy byłem zestresowany, ale później wszystko się poprawiło, a wieczorem poczułem się lepiej.	2025-01-21 08:00:00	negative_sentiment	1
54	Dziś poczułem się trochę przytłoczony. Było wiele rzeczy do zrobienia, a w pracy pojawiły się niespodziewane problemy. Na szczęście wieczorem udało mi się zrelaksować.	2024-12-28 18:30:00	negative_sentiment	1
66	Rano miałem trudną rozmowę z przełożonym, co mnie trochę zdenerwowało. Później wszystko się uspokoiło. Wieczorem poczułem ulgę i odpoczynek.	2024-12-16 19:30:00	negative_sentiment	1
4	Spędziłem popołudnie z przyjaciółmi. Rozmawialiśmy, śmialiśmy się i graliśmy w planszówki. Czuję się szczęśliwy i pełen energii.	2025-01-04 16:00:00	positive_sentiment	1
5	Poranek był stresujący z powodu pracy, ale popołudnie przyniosło ulgę. Spacer po lesie pozwolił mi się zrelaksować i poczuć lepiej.	2025-01-05 11:30:00	positive_sentiment	1
7	Czuję się trochę zmęczony po całym dniu pracy. Wieczorem obejrzałem ulubiony serial, co pomogło mi się odprężyć i poprawić nastrój.	2025-01-07 19:00:00	positive_sentiment	1
9	Spotkałem dzisiaj znajomego, z którym dawno się nie widziałem. Miło było porozmawiać i nadrobić zaległości. Czuję się pełen radości.	2025-01-09 15:45:00	positive_sentiment	1
10	Cały dzień pracowałem nad ważnym projektem. Mimo zmęczenia jestem z siebie dumny, bo zrobiłem duży postęp. Czuję się zmotywowany.	2025-01-10 20:10:00	positive_sentiment	1
12	Popołudnie spędziłem na zakupach. Udało mi się znaleźć świetne okazje i jestem z tego powodu bardzo zadowolony.	2025-01-12 14:50:00	positive_sentiment	1
13	Dziś wieczorem zagrałem w gry komputerowe. To była świetna rozrywka i relaks po długim dniu pracy. Czuję się bardziej wypoczęty.	2025-01-13 18:40:00	positive_sentiment	1
14	Poranek był zimny i deszczowy, ale mimo tego udało mi się pójść na siłownię. Czuję się pełen energii po dobrym treningu.	2025-01-14 09:15:00	positive_sentiment	1
15	Dziś miałem dzień pełen spotkań. Było trochę stresująco, ale ostatecznie udało się załatwić wszystkie ważne sprawy. Czuję ulgę.	2025-01-15 17:25:00	positive_sentiment	1
16	Odwiedziłem dzisiaj muzeum. Było dużo ciekawych eksponatów, które mnie zainspirowały. Czuję się bardziej kreatywny i zmotywowany.	2025-01-16 15:00:00	positive_sentiment	1
17	Dzień spędziłem na pisaniu. Pracuję nad nowym projektem i widzę postępy. Jestem z siebie dumny i zmotywowany do dalszej pracy.	2025-01-17 11:00:00	positive_sentiment	1
18	Czułem się dziś trochę przytłoczony obowiązkami, ale wieczorem poszedłem na spacer i wszystko stało się prostsze. Czuję się spokojniejszy.	2025-01-18 19:10:00	positive_sentiment	1
19	Dziś udało mi się skończyć książkę, którą czytałem od tygodnia. Historia była niesamowita, a ja czuję się bardzo zadowolony.	2025-01-19 21:00:00	positive_sentiment	1
20	Rano spotkałem się z przyjacielem na kawę. Rozmawialiśmy o życiu i planach na przyszłość. Czuję się zmotywowany i pełen energii.	2025-01-20 10:30:00	positive_sentiment	1
21	Dziś spędziłem czas na gotowaniu. Przygotowałem nowy przepis, który wyszedł naprawdę smaczny. Czuję się dumny ze swoich kulinarnych umiejętności.	2025-01-21 13:00:00	positive_sentiment	1
23	Dzień rozpocząłem od jogi. Pomogło mi to zrelaksować się i rozpocząć dzień w dobrym nastroju. Czuję się spokojniejszy i pełen energii.	2025-01-23 08:00:00	positive_sentiment	1
25	Dziś był bardzo intensywny dzień. Rano poszedłem na spacer, a potem miałem dużo pracy. Czułem się trochę zmęczony, ale udało mi się skończyć wszystko na czas. Dzień kończę z poczuciem satysfakcji.	2025-01-26 08:00:00	positive_sentiment	1
26	Dzisiaj byłem na spotkaniu z przyjaciółmi. Czułem się szczęśliwy, ponieważ dawno ich nie widziałem. Po spotkaniu poczułem się lekko, jakby wszystkie problemy zniknęły.	2025-01-25 19:00:00	positive_sentiment	1
27	Dzień zaczął się dość źle, miałem opóźnienie w pracy i nie mogłem się skupić. Na szczęście potem wszystko się poprawiło. Po pracy poszedłem na trening, który poprawił mi nastrój.	2025-01-24 18:30:00	positive_sentiment	1
29	Dziś był dzień pełen emocji. W pracy miałem trudną rozmowę, ale po niej poczułem ulgę. Po południu spędziłem czas z rodziną, co bardzo mnie odprężyło.	2025-01-22 21:00:00	positive_sentiment	1
32	Dziś miałem wiele spotkań w pracy. Było dość stresująco, ale udało mi się załatwić wszystkie sprawy. Czułem się zmęczony, ale zadowolony.	2025-01-19 17:30:00	positive_sentiment	1
34	W pracy dzisiaj było bardzo napięte. Miałem kilka trudnych sytuacji, ale udało mi się je rozwiązać. Czułem się zadowolony, choć zmęczony.	2025-01-17 14:45:00	positive_sentiment	1
35	Dziś miałem spokojny dzień w pracy. Nie było żadnych dużych wyzwań, więc udało mi się zrealizować wszystkie zadania. Czułem się zadowolony i zrelaksowany.	2025-01-16 09:30:00	positive_sentiment	1
36	Rano czułem się trochę znużony, ale potem poszedłem na spacer, który poprawił mi humor. Po południu miałem spotkanie, które poszło dobrze. Dzień minął szybko.	2025-01-16 09:30:00	positive_sentiment	1
73	Dziś był dzień pełen emocji. Spędziłem go w towarzystwie przyjaciół i rodziny. Czułem się bardzo kochany i doceniany. To był naprawdę dobry dzień.	2024-12-09 21:00:00	positive_sentiment	1
38	Czułem się bardzo szczęśliwy dzisiaj, ponieważ udało mi się zakończyć projekt, nad którym pracowałem od tygodnia. Dzień minął pod znakiem radości i satysfakcji.	2025-01-13 18:00:00	positive_sentiment	1
41	Rano byłem pełen energii, ale dzień w pracy okazał się bardzo długi. Na szczęście wieczorem spotkałem się z rodziną, co poprawiło mi humor.	2025-01-10 19:30:00	positive_sentiment	1
43	Dzień minął w miarę spokojnie. Miałem czas na odpoczynek, a potem spotkałem się z przyjaciółmi. Czułem się szczęśliwy, choć trochę zmęczony.	2025-01-08 20:00:00	positive_sentiment	1
11	Dzień rozpoczął się spokojnie od filiżanki herbaty. Potem zrobiłem porządki w mieszkaniu. Czuję się uporządkowany i gotowy na nowy tydzień.	2025-01-11 08:20:00	negative_sentiment	1
22	Przez cały dzień padał śnieg. Wybrałem się na spacer po zaśnieżonym parku. Krajobraz był piękny, a ja czuję się pełen podziwu.	2025-01-22 14:40:00	negative_sentiment	1
33	Dziś spędziłem dzień na świeżym powietrzu. Pogoda była piękna i to poprawiło mi nastrój. Po powrocie do domu czułem się odprężony i pełen energii.	2025-01-18 15:00:00	negative_sentiment	1
45	Dziś cały dzień spędziłem w pracy. Było dość intensywnie, ale udało mi się zrobić wszystko na czas. Czułem się zmęczony, ale zadowolony z efektów.	2025-01-06 18:00:00	positive_sentiment	1
46	Dziś miałem okazję spotkać się ze starymi znajomymi. Czułem się bardzo szczęśliwy, bo minęło dużo czasu od ostatniego spotkania. Wieczorem byłem pełen pozytywnej energii.	2025-01-05 21:30:00	positive_sentiment	1
47	Dzień był pełen wrażeń. Miałem wiele spotkań w pracy, ale wszystko poszło dobrze. Czułem się trochę zmęczony, ale ogólnie byłem zadowolony z osiągnięć.	2025-01-04 19:00:00	positive_sentiment	1
48	Dziś byłem na długim spacerze w parku. Pogoda była piękna, co poprawiło mi nastrój. Po powrocie do domu czułem się zrelaksowany i szczęśliwy.	2025-01-03 14:00:00	positive_sentiment	1
49	Dziś miałem dużo pracy, ale w końcu udało mi się skończyć wszystkie zadania. Czułem się zmęczony, ale satysfakcjonująco. Wieczorem odpocząłem przy książce.	2025-01-02 20:00:00	positive_sentiment	1
52	W pracy dzisiaj było spokojnie. Udało mi się zrobić wszystkie zadania, więc poczułem się produktywnie. Na koniec dnia byłem trochę zmęczony, ale zadowolony.	2024-12-30 19:00:00	positive_sentiment	1
53	Dziś miałem dzień pełen refleksji. Po pracy spędziłem czas na rozmyślaniach o przyszłości. Czułem się spokojnie, ale też nieco melancholijnie.	2024-12-29 21:00:00	positive_sentiment	1
55	Dziś miałem bardzo spokojny dzień. Pracowałem nad projektem, który nie wymagał dużego wysiłku, więc czułem się zrelaksowany. Po pracy udało mi się odpocząć.	2024-12-27 15:30:00	positive_sentiment	1
56	Rano wstałem pełen energii, ale później w pracy pojawiły się trudności. Na szczęście udało mi się rozwiązać problem. Wieczorem poczułem się zadowolony.	2024-12-26 18:00:00	positive_sentiment	1
57	Dziś spędziłem dzień z rodziną. Było dużo śmiechu i zabawy. Czułem się szczęśliwy i pełen energii, a wieczorem miałem poczucie, że dzień był idealny.	2024-12-25 20:00:00	positive_sentiment	1
59	Dziś miałem długi dzień w pracy. Chociaż poczułem się wyczerpany, to wszystko poszło zgodnie z planem. Na koniec dnia byłem zadowolony z wyników.	2024-12-23 19:00:00	positive_sentiment	1
61	Dziś spędziłem czas w gronie przyjaciół. Czułem się bardzo radosny i pełen energii. To był naprawdę dobry dzień, pełen śmiechu i wspólnych chwil.	2024-12-21 21:00:00	positive_sentiment	1
62	Dziś miałem sporo obowiązków w pracy, ale udało mi się wszystko skończyć na czas. Po pracy poczułem się trochę zmęczony, ale zadowolony z tego, co zrobiłem.	2024-12-20 18:00:00	positive_sentiment	1
64	Rano było dość cicho i spokojnie, więc miałem czas na refleksję. Dzień w pracy minął bez większych trudności. Czułem się neutralnie, ale zrelaksowany.	2024-12-18 08:30:00	positive_sentiment	1
65	Dziś miałem dzień pełen zajęć. W pracy było trochę zamieszania, ale udało mi się wszystko ogarnąć. Po pracy poszedłem na spacer, żeby się zrelaksować.	2024-12-17 17:00:00	positive_sentiment	1
67	Dziś miałem całkiem spokojny dzień w pracy. Spędziłem go na pracy nad dokumentami, co nie było bardzo ekscytujące, ale przynajmniej wszystko szło zgodnie z planem.	2024-12-15 15:00:00	positive_sentiment	1
68	Czułem się dziś bardzo szczęśliwy, ponieważ udało mi się zakończyć projekt, nad którym pracowałem przez długi czas. Dzień minął w miłej atmosferze i z poczuciem spełnienia.	2024-12-14 18:45:00	positive_sentiment	1
71	Dziś czułem się pełen energii! Spędziłem cały dzień na świeżym powietrzu, co poprawiło mi nastrój. Po powrocie do domu czułem się radosny i zrelaksowany.	2024-12-11 16:00:00	positive_sentiment	1
72	Rano miałem dużo do zrobienia, ale cały dzień minął bardzo szybko. W pracy pojawiły się wyzwania, ale udało mi się je pokonać. Czułem się zmęczony, ale dumny.	2024-12-10 18:30:00	positive_sentiment	1
75	Dziś miałem dzień pełen refleksji. Spędziłem trochę czasu w ciszy, myśląc o przeszłości. Czułem się spokojnie, ale również nieco nostalgicznie.	2024-12-07 14:00:00	positive_sentiment	1
76	Dziś spędziłem większość dnia w pracy, ale udało mi się znaleźć chwilę na odpoczynek. Wieczorem spotkałem się z przyjaciółmi, co poprawiło mi nastrój.	2024-12-06 19:00:00	positive_sentiment	1
77	Rano miałem spotkanie, które trochę mnie stresowało. Na szczęście później wszystko się uspokoiło. Po pracy poczułem się zmęczony, ale zadowolony z efektów.	2024-12-05 08:30:00	positive_sentiment	1
79	Dziś miałem dość intensywny dzień. W pracy pojawiły się trudności, ale udało mi się je pokonać. Wieczorem spędziłem czas na relaksie, co pozwoliło mi się zregenerować.	2024-12-03 20:00:00	positive_sentiment	1
80	Rano czułem się dość zmęczony, ale potem poszedłem na spacer, co poprawiło mi nastrój. Po pracy spędziłem czas z rodziną, co sprawiło, że poczułem się szczęśliwy.	2024-12-02 18:00:00	positive_sentiment	1
81	Dziś dzień minął bardzo spokojnie. Spędziłem go na pracy w ogrodzie, co bardzo mnie odprężyło. Czułem się zadowolony, ale trochę zmęczony fizycznie.	2024-12-01 16:30:00	positive_sentiment	1
82	Dziś w pracy było sporo zamieszania. Miałem wiele zadań do wykonania, ale na szczęście udało mi się je zakończyć na czas. Czułem się trochę zestresowany, ale zadowolony.	2024-11-30 18:30:00	positive_sentiment	1
83	Dziś byłem na spotkaniu z przyjaciółmi, co bardzo poprawiło mi nastrój. Czułem się szczęśliwy, ale wieczorem poczułem lekki zmęczenie po całym dniu.	2024-11-29 21:00:00	positive_sentiment	1
84	Dziś rano miałem trudności z rozpoczęciem dnia, ale później wszystko się poprawiło. Wieczorem poczułem się spokojnie i pełen energii, gotowy na kolejny dzień.	2024-11-28 19:00:00	positive_sentiment	1
87	Dziś spędziłem dzień w gronie rodziny. Było to bardzo miłe doświadczenie. Czułem się kochany i doceniany, a wieczorem byłem pełen pozytywnej energii.	2024-11-25 21:00:00	positive_sentiment	1
88	Dziś w pracy pojawiły się pewne trudności, które musiałem szybko rozwiązać. Czułem się zestresowany, ale pod koniec dnia poczułem ulgę i satysfakcję z wykonanej pracy.	2024-11-24 18:30:00	positive_sentiment	1
90	Dziś miałem pełny dzień w pracy, ale udało mi się zrobić wszystko na czas. Czułem się zmęczony, ale zadowolony z tego, co udało mi się osiągnąć.	2024-11-22 19:00:00	positive_sentiment	1
91	Dziś rano miałem trudności z rozpoczęciem dnia, ale potem wszystko poszło gładko. Spędziłem resztę dnia w pracy, kończąc zadania, które były na mojej liście.	2024-11-21 08:00:00	positive_sentiment	1
51	Dziś spędziłem czas w kuchni, przygotowując coś pysznego. Czułem się dobrze, choć trochę samotnie. Jednak gotowanie zawsze poprawia mi humor.	2024-12-31 17:30:00	negative_sentiment	1
92	Dziś było w pracy spokojnie, choć nie brakowało drobnych problemów. Czułem się trochę zmęczony, ale zadowolony z postępów. Wieczorem odpoczywałem przy filmie.	2024-11-20 20:00:00	positive_sentiment	1
93	Dziś poczułem się naprawdę dobrze, ponieważ udało mi się zakończyć projekt, nad którym pracowałem przez dłuższy czas. Dzień minął w dobrym nastroju i poczuciu sukcesu.	2024-11-19 17:30:00	positive_sentiment	1
94	Dziś spędziłem dzień na zewnątrz, spacerując po lesie. Czułem się naprawdę zrelaksowany, a kontakt z naturą dodał mi energii na resztę dnia.	2024-11-18 15:00:00	positive_sentiment	1
97	Dziś miałem spotkanie, które mnie trochę stresowało, ale na szczęście wszystko poszło dobrze. Po pracy poczułem ulgę i odpoczynek, czułem się zadowolony.	2024-11-15 19:30:00	positive_sentiment	1
98	Dziś w pracy było dość spokojnie. Spędziłem czas na organizowaniu rzeczy, co pozwoliło mi poczuć się bardziej zorganizowanym. Czułem się zrelaksowany i spokojny.	2024-11-14 18:00:00	positive_sentiment	1
99	Dziś miałem bardzo intensywny dzień w pracy. Było wiele do zrobienia, ale wszystko udało mi się zrobić na czas. Wieczorem byłem zmęczony, ale zadowolony z efektów.	2024-11-13 20:00:00	positive_sentiment	1
100	Dziś spędziłem czas z rodziną. To był bardzo miły dzień pełen śmiechu i rozmów. Czułem się kochany i doceniany, co poprawiło mi nastrój na resztę dnia.	2024-11-12 21:00:00	positive_sentiment	1
101	Rano czułem się trochę zmęczony, ale w pracy wszystko szło zgodnie z planem. Później spotkałem się z przyjaciółmi, co poprawiło mi humor.	2024-11-11 19:00:00	positive_sentiment	1
102	Dziś miałem dzień pełen zadania do wykonania w pracy. Mimo że dzień był długi, czułem się produktywny. Wieczorem odpocząłem przy książce.	2024-11-10 18:30:00	positive_sentiment	1
103	Dziś miałem świetny dzień! Spędziłem go na świeżym powietrzu, uprawiając sport. Czułem się pełen energii i radości. Wieczorem byłem naprawdę zadowolony.	2024-11-09 15:30:00	positive_sentiment	1
104	Dziś był dzień pełen pracy. Czułem się trochę przytłoczony ilością zadań, ale na koniec dnia udało mi się zrealizować wszystko, co zaplanowałem. Byłem zmęczony, ale zadowolony.	2024-11-08 20:00:00	positive_sentiment	1
106	Spędziłem dzień z rodziną. Po obiedzie poszliśmy na wspólny spacer. Czułem się naprawdę szczęśliwy i pełen miłości do bliskich.	2025-01-25 15:00:00	positive_sentiment	1
107	Dziś był dzień pełen pracy. Mimo dużego natłoku obowiązków udało mi się wszystko skończyć na czas. Czuję się zadowolony i trochę zmęczony.	2025-01-24 19:30:00	positive_sentiment	1
108	Rano miałem ciężki poranek, bo źle się wyspałem. Na szczęście, popołudniu zrobiłem sobie chwilę przerwy i poczułem się lepiej.	2025-01-23 10:00:00	positive_sentiment	1
125	To jest wiadomość testowa	2025-01-20 21:17:21	neutral_sentiment	1
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, email, password, name, last_name) FROM stdin;
1	qwerty@gmail.com	$2b$12$dPEyoX16QZHxHFaouhTkO.eIrMBFWfrdTBZUY4YavF2EdWRC/OIee	Nazar	Kuziv
\.


--
-- Name: diaries_entries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.diaries_entries_id_seq', 144, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 36, true);


--
-- Name: diaries_entries diaries_entries_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diaries_entries
    ADD CONSTRAINT diaries_entries_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: diaries_entries fk_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diaries_entries
    ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

