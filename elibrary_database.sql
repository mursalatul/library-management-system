PGDMP  ,    (                |            elibrary    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    elibrary    DATABASE     �   CREATE DATABASE elibrary WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE elibrary;
                postgres    false            �            1259    16399    login    TABLE     �   CREATE TABLE public.login (
    libraryid character varying(20) NOT NULL,
    username character varying(20),
    password character varying(20)
);
    DROP TABLE public.login;
       public         heap    postgres    false            �            1259    16409    login_admin    TABLE     �   CREATE TABLE public.login_admin (
    admin_id character varying(20) NOT NULL,
    username character varying(20),
    password character varying(20)
);
    DROP TABLE public.login_admin;
       public         heap    postgres    false            �            1259    16404    user_info_basic    TABLE     �   CREATE TABLE public.user_info_basic (
    libraryid character varying(20) NOT NULL,
    firstname character varying(20),
    lastname character varying(20),
    username character varying(20)
);
 #   DROP TABLE public.user_info_basic;
       public         heap    postgres    false            �          0    16399    login 
   TABLE DATA           >   COPY public.login (libraryid, username, password) FROM stdin;
    public          postgres    false    215   w       �          0    16409    login_admin 
   TABLE DATA           C   COPY public.login_admin (admin_id, username, password) FROM stdin;
    public          postgres    false    217   �       �          0    16404    user_info_basic 
   TABLE DATA           S   COPY public.user_info_basic (libraryid, firstname, lastname, username) FROM stdin;
    public          postgres    false    216   �       \           2606    16413    login_admin login_admin_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.login_admin
    ADD CONSTRAINT login_admin_pkey PRIMARY KEY (admin_id);
 F   ALTER TABLE ONLY public.login_admin DROP CONSTRAINT login_admin_pkey;
       public            postgres    false    217            X           2606    16403    login login_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (libraryid);
 :   ALTER TABLE ONLY public.login DROP CONSTRAINT login_pkey;
       public            postgres    false    215            Z           2606    16408 $   user_info_basic user_info_basic_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.user_info_basic
    ADD CONSTRAINT user_info_basic_pkey PRIMARY KEY (libraryid);
 N   ALTER TABLE ONLY public.user_info_basic DROP CONSTRAINT user_info_basic_pkey;
       public            postgres    false    216            �      x�K4�,�(p0����� ��      �      x�K.N5��K�����s0����� ?      �   $   x�K4��--*N�I,)��H���O�,������ �ST     