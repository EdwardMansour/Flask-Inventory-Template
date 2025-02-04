--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

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
-- Name: userrole; Type: TYPE; Schema: public; Owner: anonymous
--

CREATE TYPE public.userrole AS ENUM (
    'ADMIN',
    'REGULAR'
);


ALTER TYPE public.userrole OWNER TO anonymous;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: anonymous
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO anonymous;

--
-- Name: product; Type: TABLE; Schema: public; Owner: anonymous
--

CREATE TABLE public.product (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    amount double precision NOT NULL,
    is_destroyed boolean NOT NULL,
    user_id integer NOT NULL,
    expiry_date date
);


ALTER TABLE public.product OWNER TO anonymous;

--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: anonymous
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.product_id_seq OWNER TO anonymous;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anonymous
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: anonymous
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(80) NOT NULL,
    date_of_birth date NOT NULL,
    role public.userrole NOT NULL,
    password_hash character varying(128) NOT NULL
);


ALTER TABLE public."user" OWNER TO anonymous;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: anonymous
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_id_seq OWNER TO anonymous;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anonymous
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: product id; Type: DEFAULT; Schema: public; Owner: anonymous
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: anonymous
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: anonymous
--

COPY public.alembic_version (version_num) FROM stdin;
d7c6e469d11b
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: anonymous
--

COPY public.product (id, name, amount, is_destroyed, user_id, expiry_date) FROM stdin;
1	item-1-1	2.5	f	2	2024-11-14
2	item-1-2	2.5	f	2	2024-11-14
3	item-1-3	2.5	f	2	2024-11-14
4	item-1-4	2.5	f	2	2024-11-14
5	item-1-5	2.5	f	2	2024-11-14
6	item-1	2.5	f	1	2024-11-14
7	item-2	2.5	f	1	2024-11-14
8	item-3	2.5	f	1	2024-11-14
9	item-4	2.5	f	1	2024-11-14
10	item-5	2.5	f	1	2024-11-14
11	item-1-admin	2.5	f	3	2024-11-14
12	item-2-admin	2.5	f	3	2024-11-14
13	item-3-admin	2.5	f	3	2024-11-14
14	item-4-admin	2.5	f	3	2024-11-14
15	item-5-admin	2.5	f	3	2024-11-14
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: anonymous
--

COPY public."user" (id, username, date_of_birth, role, password_hash) FROM stdin;
1	edward	1996-01-17	REGULAR	$2b$12$wv7dLp1YiBQyQAH27Cars.2E1O6UJI7ZotjzoXb0EFTjfOh/7zBnW
2	edward-1	1996-01-17	REGULAR	$2b$12$tCtcXMGalF5zvL3jQ0vHbe9bg7v8lolbncubfzqkM4JFevlXYFhFa
3	admin	2024-10-04	ADMIN	$2b$12$Y1BWd5uFcFXEyzDnKxU.YuwIdaODwaS5EACqyH2ZSjq.B8SxoTccq
\.


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anonymous
--

SELECT pg_catalog.setval('public.product_id_seq', 15, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anonymous
--

SELECT pg_catalog.setval('public.user_id_seq', 3, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: anonymous
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: anonymous
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: anonymous
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: anonymous
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: product product_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anonymous
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- PostgreSQL database dump complete
--

