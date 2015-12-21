--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

ALTER TABLE ONLY public.ventas_detalleventa DROP CONSTRAINT ventas_detallevent_venta_id_40e30ceafe7e4dbd_fk_ventas_venta_id;
ALTER TABLE ONLY public.ventas_detalleventa DROP CONSTRAINT ventas_detalle_producto_id_118158844bdb77dc_fk_producto_item_id;
ALTER TABLE ONLY public.proveedores_proveedor DROP CONSTRAINT proveedores_proveedor_user_id_228f2e62237ca3ef_fk_auth_user_id;
ALTER TABLE ONLY public.producto_item DROP CONSTRAINT producto_item_user_id_6d48f690ae37d8e0_fk_auth_user_id;
ALTER TABLE ONLY public.producto_item DROP CONSTRAINT produ_proveedor_id_2e3a63b725ac1d76_fk_proveedores_proveedor_id;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id;
ALTER TABLE ONLY public.compras_detallecompra DROP CONSTRAINT compras_detalle_compra_id_260163a87f2dc4c4_fk_compras_compra_id;
ALTER TABLE ONLY public.compras_detallecompra DROP CONSTRAINT compras_detall_producto_id_70cc5b8fd5c40dd8_fk_producto_item_id;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id;
ALTER TABLE ONLY public.almacenes_item DROP CONSTRAINT almac_proveedor_id_65c436bdd42a4286_fk_proveedores_proveedor_id;
DROP INDEX public.ventas_detalleventa_bb91903a;
DROP INDEX public.ventas_detalleventa_a3d89257;
DROP INDEX public.proveedores_proveedor_e8701ad4;
DROP INDEX public.producto_item_e8701ad4;
DROP INDEX public.producto_item_7ac33b97;
DROP INDEX public.django_session_session_key_461cfeaa630ca218_like;
DROP INDEX public.django_session_de54fa62;
DROP INDEX public.django_admin_log_e8701ad4;
DROP INDEX public.django_admin_log_417f1b1c;
DROP INDEX public.compras_detallecompra_bb91903a;
DROP INDEX public.compras_detallecompra_98926b7a;
DROP INDEX public.auth_user_username_51b3b110094b8aae_like;
DROP INDEX public.auth_user_user_permissions_e8701ad4;
DROP INDEX public.auth_user_user_permissions_8373b171;
DROP INDEX public.auth_user_groups_e8701ad4;
DROP INDEX public.auth_user_groups_0e939a4f;
DROP INDEX public.auth_permission_417f1b1c;
DROP INDEX public.auth_group_permissions_8373b171;
DROP INDEX public.auth_group_permissions_0e939a4f;
DROP INDEX public.auth_group_name_253ae2a6331666e8_like;
DROP INDEX public.almacenes_item_7ac33b97;
ALTER TABLE ONLY public.ventas_venta DROP CONSTRAINT ventas_venta_pkey;
ALTER TABLE ONLY public.ventas_detalleventa DROP CONSTRAINT ventas_detalleventa_pkey;
ALTER TABLE ONLY public.proveedores_proveedor DROP CONSTRAINT proveedores_proveedor_pkey;
ALTER TABLE ONLY public.proveedores_proveedor DROP CONSTRAINT proveedores_proveedor_codigo_4566124652cfe34a_uniq;
ALTER TABLE ONLY public.producto_item DROP CONSTRAINT producto_item_pkey;
ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
ALTER TABLE ONLY public.compras_detallecompra DROP CONSTRAINT compras_detallecompra_pkey;
ALTER TABLE ONLY public.compras_compra DROP CONSTRAINT compras_compra_pkey;
ALTER TABLE ONLY public.cliente_cliente DROP CONSTRAINT cliente_cliente_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_key;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_key;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_key;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
ALTER TABLE ONLY public.almacenes_item DROP CONSTRAINT almacenes_item_pkey;
ALTER TABLE public.ventas_venta ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.ventas_detalleventa ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.proveedores_proveedor ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.producto_item ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.compras_detallecompra ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.compras_compra ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.cliente_cliente ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.almacenes_item ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE public.ventas_venta_id_seq;
DROP TABLE public.ventas_venta;
DROP SEQUENCE public.ventas_detalleventa_id_seq;
DROP TABLE public.ventas_detalleventa;
DROP SEQUENCE public.proveedores_proveedor_id_seq;
DROP TABLE public.proveedores_proveedor;
DROP SEQUENCE public.producto_item_id_seq;
DROP TABLE public.producto_item;
DROP TABLE public.django_session;
DROP SEQUENCE public.django_migrations_id_seq;
DROP TABLE public.django_migrations;
DROP SEQUENCE public.django_content_type_id_seq;
DROP TABLE public.django_content_type;
DROP SEQUENCE public.django_admin_log_id_seq;
DROP TABLE public.django_admin_log;
DROP SEQUENCE public.compras_detallecompra_id_seq;
DROP TABLE public.compras_detallecompra;
DROP SEQUENCE public.compras_compra_id_seq;
DROP TABLE public.compras_compra;
DROP SEQUENCE public.cliente_cliente_id_seq;
DROP TABLE public.cliente_cliente;
DROP SEQUENCE public.auth_user_user_permissions_id_seq;
DROP TABLE public.auth_user_user_permissions;
DROP SEQUENCE public.auth_user_id_seq;
DROP SEQUENCE public.auth_user_groups_id_seq;
DROP TABLE public.auth_user_groups;
DROP TABLE public.auth_user;
DROP SEQUENCE public.auth_permission_id_seq;
DROP TABLE public.auth_permission;
DROP SEQUENCE public.auth_group_permissions_id_seq;
DROP TABLE public.auth_group_permissions;
DROP SEQUENCE public.auth_group_id_seq;
DROP TABLE public.auth_group;
DROP SEQUENCE public.almacenes_item_id_seq;
DROP TABLE public.almacenes_item;
DROP EXTENSION plpgsql;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: almacenes_item; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE almacenes_item (
    id integer NOT NULL,
    codigo_item character varying(10) NOT NULL,
    codigo_fabrica character varying(10) NOT NULL,
    almacen integer NOT NULL,
    grupo character varying(50) NOT NULL,
    subgrupo character varying(50) NOT NULL,
    descripcion character varying(200) NOT NULL,
    carac_especial_1 character varying(50) NOT NULL,
    carac_especial_2 character varying(50) NOT NULL,
    cantidad integer NOT NULL,
    saldo_min integer NOT NULL,
    imagen character varying(100) NOT NULL,
    unidad_medida character varying(20) NOT NULL,
    costo_unitario numeric(5,3) NOT NULL,
    proveedor_id integer NOT NULL
);


ALTER TABLE public.almacenes_item OWNER TO root;

--
-- Name: almacenes_item_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE almacenes_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.almacenes_item_id_seq OWNER TO root;

--
-- Name: almacenes_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE almacenes_item_id_seq OWNED BY almacenes_item.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO root;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO root;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO root;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO root;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO root;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO root;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO root;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO root;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO root;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO root;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO root;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO root;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: cliente_cliente; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE cliente_cliente (
    id integer NOT NULL,
    codigo character varying(50) NOT NULL,
    razonsocial character varying(50) NOT NULL,
    nit integer NOT NULL,
    direccion character varying(50) NOT NULL,
    telefonos1 character varying(8) NOT NULL,
    telefonos2 character varying(8) NOT NULL,
    telefonos3 character varying(8) NOT NULL,
    contacto character varying(50) NOT NULL,
    rubro character varying(50) NOT NULL,
    categoria character varying(50) NOT NULL,
    ubucaciongeo character varying(50) NOT NULL,
    fecha date NOT NULL,
    fecha2 date NOT NULL,
    textos character varying(50) NOT NULL,
    textos2 character varying(50) NOT NULL
);


ALTER TABLE public.cliente_cliente OWNER TO root;

--
-- Name: cliente_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE cliente_cliente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cliente_cliente_id_seq OWNER TO root;

--
-- Name: cliente_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE cliente_cliente_id_seq OWNED BY cliente_cliente.id;


--
-- Name: compras_compra; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE compras_compra (
    id integer NOT NULL,
    nit integer NOT NULL,
    razon_social character varying(100) NOT NULL,
    nro_factura integer NOT NULL,
    nro_autorizacion character varying(20) NOT NULL,
    fecha date NOT NULL,
    cod_control character varying(100) NOT NULL,
    total numeric(8,2),
    cantidad_dias integer NOT NULL,
    tipo_compra character varying(100) NOT NULL
);


ALTER TABLE public.compras_compra OWNER TO root;

--
-- Name: compras_compra_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE compras_compra_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.compras_compra_id_seq OWNER TO root;

--
-- Name: compras_compra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE compras_compra_id_seq OWNED BY compras_compra.id;


--
-- Name: compras_detallecompra; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE compras_detallecompra (
    id integer NOT NULL,
    codigo character varying(100) NOT NULL,
    cantidad integer NOT NULL,
    unidad character varying(10) NOT NULL,
    detalle character varying(100) NOT NULL,
    precio_unitario numeric(6,2) NOT NULL,
    subtotal numeric(6,2) NOT NULL,
    descuento numeric(6,2) NOT NULL,
    recargo numeric(6,2) NOT NULL,
    ice numeric(6,2) NOT NULL,
    excentos numeric(6,2) NOT NULL,
    scf numeric(6,2) NOT NULL,
    centro_costos character varying(100) NOT NULL,
    compra_id integer NOT NULL,
    producto_id integer,
    tipo_descuento character varying(100) NOT NULL,
    tipo_recargo character varying(100) NOT NULL
);


ALTER TABLE public.compras_detallecompra OWNER TO root;

--
-- Name: compras_detallecompra_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE compras_detallecompra_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.compras_detallecompra_id_seq OWNER TO root;

--
-- Name: compras_detallecompra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE compras_detallecompra_id_seq OWNED BY compras_detallecompra.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO root;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO root;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO root;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO root;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO root;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO root;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO root;

--
-- Name: producto_item; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE producto_item (
    id integer NOT NULL,
    codigo_item character varying(100) NOT NULL,
    codigo_fabrica character varying(100) NOT NULL,
    almacen integer NOT NULL,
    grupo character varying(100) NOT NULL,
    subgrupo character varying(100) NOT NULL,
    descripcion character varying(200) NOT NULL,
    carac_especial_1 character varying(100) NOT NULL,
    carac_especial_2 character varying(100) NOT NULL,
    cantidad integer NOT NULL,
    saldo_min integer NOT NULL,
    imagen character varying(100),
    unidad_medida character varying(100) NOT NULL,
    costo_unitario numeric(6,2) NOT NULL,
    precio_unitario numeric(6,2) NOT NULL,
    proveedor_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.producto_item OWNER TO root;

--
-- Name: producto_item_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE producto_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producto_item_id_seq OWNER TO root;

--
-- Name: producto_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE producto_item_id_seq OWNED BY producto_item.id;


--
-- Name: proveedores_proveedor; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE proveedores_proveedor (
    id integer NOT NULL,
    codigo character varying(20) NOT NULL,
    razon_social character varying(150) NOT NULL,
    nit character varying(20) NOT NULL,
    direccion character varying(50) NOT NULL,
    telefono1 integer NOT NULL,
    telefono2 integer,
    telefono3 integer,
    contactos character varying(150) NOT NULL,
    rubro character varying(50) NOT NULL,
    ubicacion_geo character varying(50) NOT NULL,
    fecha1 date NOT NULL,
    fecha2 date NOT NULL,
    texto1 character varying(50),
    texto2 character varying(50),
    user_id integer NOT NULL
);


ALTER TABLE public.proveedores_proveedor OWNER TO root;

--
-- Name: proveedores_proveedor_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE proveedores_proveedor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proveedores_proveedor_id_seq OWNER TO root;

--
-- Name: proveedores_proveedor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE proveedores_proveedor_id_seq OWNED BY proveedores_proveedor.id;


--
-- Name: ventas_detalleventa; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE ventas_detalleventa (
    id integer NOT NULL,
    cantidad integer NOT NULL,
    subtotal numeric(6,2) NOT NULL,
    descuento numeric(6,2) NOT NULL,
    recargo numeric(6,2) NOT NULL,
    ice numeric(6,2) NOT NULL,
    excentos numeric(6,2) NOT NULL,
    scf numeric(6,2) NOT NULL,
    producto_id integer NOT NULL,
    venta_id integer NOT NULL,
    tipo_descuento character varying(100) NOT NULL,
    tipo_recargo character varying(100) NOT NULL
);


ALTER TABLE public.ventas_detalleventa OWNER TO root;

--
-- Name: ventas_detalleventa_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE ventas_detalleventa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ventas_detalleventa_id_seq OWNER TO root;

--
-- Name: ventas_detalleventa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE ventas_detalleventa_id_seq OWNED BY ventas_detalleventa.id;


--
-- Name: ventas_venta; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE ventas_venta (
    id integer NOT NULL,
    fecha date NOT NULL,
    nit integer NOT NULL,
    razon_social character varying(100) NOT NULL,
    tipo_compra character varying(100) NOT NULL,
    cantidad_dias integer NOT NULL,
    total numeric(8,2)
);


ALTER TABLE public.ventas_venta OWNER TO root;

--
-- Name: ventas_venta_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE ventas_venta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ventas_venta_id_seq OWNER TO root;

--
-- Name: ventas_venta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE ventas_venta_id_seq OWNED BY ventas_venta.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY almacenes_item ALTER COLUMN id SET DEFAULT nextval('almacenes_item_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY cliente_cliente ALTER COLUMN id SET DEFAULT nextval('cliente_cliente_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY compras_compra ALTER COLUMN id SET DEFAULT nextval('compras_compra_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY compras_detallecompra ALTER COLUMN id SET DEFAULT nextval('compras_detallecompra_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY producto_item ALTER COLUMN id SET DEFAULT nextval('producto_item_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY proveedores_proveedor ALTER COLUMN id SET DEFAULT nextval('proveedores_proveedor_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY ventas_detalleventa ALTER COLUMN id SET DEFAULT nextval('ventas_detalleventa_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY ventas_venta ALTER COLUMN id SET DEFAULT nextval('ventas_venta_id_seq'::regclass);


--
-- Data for Name: almacenes_item; Type: TABLE DATA; Schema: public; Owner: root
--

COPY almacenes_item (id, codigo_item, codigo_fabrica, almacen, grupo, subgrupo, descripcion, carac_especial_1, carac_especial_2, cantidad, saldo_min, imagen, unidad_medida, costo_unitario, proveedor_id) FROM stdin;
\.


--
-- Name: almacenes_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('almacenes_item_id_seq', 1, false);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add libro	7	add_libro
20	Can change libro	7	change_libro
21	Can delete libro	7	delete_libro
22	Can add captcha store	8	add_captchastore
23	Can change captcha store	8	change_captchastore
24	Can delete captcha store	8	delete_captchastore
25	Can add proveedor	9	add_proveedor
26	Can change proveedor	9	change_proveedor
27	Can delete proveedor	9	delete_proveedor
28	Can add item	10	add_item
29	Can change item	10	change_item
30	Can delete item	10	delete_item
31	Can add item	11	add_item
32	Can change item	11	change_item
33	Can delete item	11	delete_item
34	Can add cliente	12	add_cliente
35	Can change cliente	12	change_cliente
36	Can delete cliente	12	delete_cliente
37	Can add compra	13	add_compra
38	Can change compra	13	change_compra
39	Can delete compra	13	delete_compra
40	Can add detalle compra	14	add_detallecompra
41	Can change detalle compra	14	change_detallecompra
42	Can delete detalle compra	14	delete_detallecompra
43	Can add venta	15	add_venta
44	Can change venta	15	change_venta
45	Can delete venta	15	delete_venta
46	Can add detalle venta	16	add_detalleventa
47	Can change detalle venta	16	change_detalleventa
48	Can delete detalle venta	16	delete_detalleventa
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_permission_id_seq', 48, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$20000$LTlYZ40Byh7s$3J3H5TUuFj7Sx/+iWECoprLEwEMAbYKg8Va84y4dH6o=	2015-12-03 17:50:20.648995-04	t	admin			josedanielf9@gmail.com	t	t	2015-08-18 17:59:04.464361-04
2	pbkdf2_sha256$20000$owfTVZrD9tL1$b/HiiaJifj2YB7JPUQuv/xLMI25WElT5/Mr1u8zwVj8=	2015-09-24 19:44:02.328286-04	f	jose				f	t	2015-09-23 17:12:21.554207-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_id_seq', 2, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: root
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: cliente_cliente; Type: TABLE DATA; Schema: public; Owner: root
--

COPY cliente_cliente (id, codigo, razonsocial, nit, direccion, telefonos1, telefonos2, telefonos3, contacto, rubro, categoria, ubucaciongeo, fecha, fecha2, textos, textos2) FROM stdin;
4	hgghj	jgjg	5454	ggfghf	646446	646	6464	hghg	ghfg	hg	hghg	2015-11-17	2015-11-17	nfhf	hfhf
5	33	wer	3232	2333	454	5445	5454	ttrrtrt	trt	fggf	gfgf	2015-11-17	2015-11-17	hghg	hghgg
6	dsd	sdsd	324234	werwer	34234	23424	234234	ewrwer	werwer	werwer	werwer	2015-11-17	2015-11-17	sfsdf	sdfs
7	sadasd	aasdas	6565	frtr	343434	43534	353	ghyt	ytyt	yty	yty	2015-11-18	2015-11-18	eeee	eeeee
8	ewwe	hghh	55	ytyty	45657558	2223332	54646464	ytytytyt	tytyt	ytyt	ytyt	2015-11-18	2015-11-18	juyyu	uyuy
9	uyuy	uyuy	554	ggfg	65656778	32432432	23423423	hghgh	hghg	hghg	hghg	2015-11-18	2015-11-18	jhjh	jh
10	uyuyu	uyuuyu	6767	hghg	45646646	1	1	ytytyty	ytyt	ytyt	yty	2015-11-18	2015-11-18	jhjhjh	jhjhj
11	ssdf	kjhjh	565	yyytt	1134444			ertet	etete	kkjkj	kjk	2015-11-18	2015-11-18	lkjk	kjk
\.


--
-- Name: cliente_cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('cliente_cliente_id_seq', 11, true);


--
-- Data for Name: compras_compra; Type: TABLE DATA; Schema: public; Owner: root
--

COPY compras_compra (id, nit, razon_social, nro_factura, nro_autorizacion, fecha, cod_control, total, cantidad_dias, tipo_compra) FROM stdin;
117	3423	sdasda	4555	32423	2015-11-16	jhjhjh	308.00	0	contado
118	2323	ewerwerw	797	4657	2015-11-16	kjkjkjk	3535.00	0	contado
119	454	jjhj	454	4646	2015-11-16	hjhjh	637.00	0	contado
120	890	gfsgsg	433534	546456	2015-11-16	dsfdsf	1309.00	0	contado
121	5656	sadasd	7899	6577	2015-11-16	jghh	567.00	0	contado
122	4677	jkjkh	675	5657	2015-11-16	khhhj	343.00	0	contado
123	67676	jhjhjh	6886	7676	2015-11-16	jjhjhj	238.00	0	contado
124	4434	hjhjh	5787	6788	2015-11-16	hghg	294.00	0	contado
125	676	jghg	56575	567575	2015-11-17	ghhgh	90.00	0	contado
126	3535	hghg	4675	575	2015-11-17	jghh	142.60	0	contado
127	324	werwe	3242	234	2015-11-18	werwr	179.00	0	contado
128	223423	hghgh	54646	454	2015-11-23	jgghg	152.00	0	contado
129	34535	ertert	34535	3535	2015-11-23	dgfdgdfgd	532.00	0	contado
130	5656	hghg	45644	46546	2015-11-23	hjjh	602.00	0	contado
131	5334	vbbvv	34646	65565	2015-11-27	vvbv	0.00	0	contado
132	4353	kjjkjk	676	7676	2015-11-27	hhgg	0.00	0	contado
133	5767	ghhfhf	546768	6578798	2015-11-27	nhghggh	900.00	0	contado
134	578	hhghg	44657	456578	2015-11-27	hghg	179.00	0	contado
135	464464	trtrrtrrt	35533553	544545	2015-11-27	hfgffgff	90.00	0	contado
136	78856	uyuy	677677	767676	2015-11-27	jjh	90.00	0	contado
137	4567	hghgh	655655	676767	2015-11-27	hgghgh	179.00	0	contado
138	56656	hgghgh	556757	755575	2015-11-27	gfgfh	179.00	0	contado
139	32423	jgjggg	67676	7575	2015-11-27	hggh	179.00	0	contado
140	6646	ghghg	5757	57533	2015-11-27	ghgjgjgjgg	179.00	0	contado
141	578885	gjgjgg	78888	7907	2015-11-27	hghggh	179.00	0	contado
142	57733	utututu	5758	58585	2015-11-27	hjgjjg	179.00	5	credito
143	678788	ghghgggh	76766676	345667777777777	2015-11-27	hjhjhjj	179.00	0	contado
144	66767766	gytyttyt	6788889	3456758687878887	2015-11-27	fgfgfgfggfff	89.00	0	contado
145	788999	ytyytyt	5755575	464646446464646	2015-11-27	ghgfgfggf	179.00	0	contado
146	566664	hhghgg	56565	56565	2015-11-27	gfgfgf	179.00	0	contado
147	324324	dfgdfgd	2424	34345353535	2015-11-28	dffdgdfg	179.00	0	contado
\.


--
-- Name: compras_compra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('compras_compra_id_seq', 147, true);


--
-- Data for Name: compras_detallecompra; Type: TABLE DATA; Schema: public; Owner: root
--

COPY compras_detallecompra (id, codigo, cantidad, unidad, detalle, precio_unitario, subtotal, descuento, recargo, ice, excentos, scf, centro_costos, compra_id, producto_id, tipo_descuento, tipo_recargo) FROM stdin;
51	AMOR0004	1	Pza	Amortiguador Trasero Ipsum P/O // KYB // Toy // KYB // Toy	189.00	189.00	0.00	0.00	0.00	0.00	189.00	A	117	2346	Bs	Bs
52	AMOR0005	10	Pza	Amortiguador Trasero  O/O // KYB // Toy // KYB // Toy	175.00	1750.00	0.00	0.00	0.00	0.00	1750.00	A	118	2347	Bs	Bs
53	AMOR0008	1	Pza	Amortiguador Direccion Mazda M/OM // TOKICO // Maz // TOKICO // Maz	448.00	448.00	0.00	0.00	0.00	0.00	448.00	A	119	2349	Bs	Bs
54	AMOR0004	1	Pza	Amortiguador Trasero Ipsum P/O // KYB // Toy // KYB // Toy	189.00	189.00	0.00	0.00	0.00	0.00	189.00	A	119	2346	Bs	Bs
55	AMOR0009	1	Pza	Amortiguador Telescopio Corolla	119.00	119.00	0.00	0.00	0.00	0.00	119.00	A	120	2350	Bs	Bs
56	AMOR0007	1	Pza	Amortiguador Direccion Lan Cruiser M/P // KYB // Toy // KYB // Toy	448.00	448.00	0.00	0.00	0.00	0.00	448.00	A	121	2348	Bs	Bs
57	AMOR0009	1	Pza	Amortiguador Telescopio Corolla	119.00	119.00	0.00	0.00	0.00	0.00	119.00	A	121	2350	Bs	Bs
58	AMOR0002	1	Pza	Amortiguador  Delantero Patrol P/P // KYB // Nis // KYB // Nis	224.00	224.00	0.00	0.00	0.00	0.00	224.00	A	122	2344	Bs	Bs
59	AMOR0009	1	Pza	Amortiguador Telescopio Corolla	119.00	119.00	0.00	0.00	0.00	0.00	119.00	A	122	2350	Bs	Bs
60	AMOR0003	1	Pza	Amortiguador Trasero  Isuzu P/OM // KYB // Isu // KYB // Isu	119.00	119.00	0.00	0.00	0.00	0.00	119.00	A	123	2345	Bs	Bs
61	AMOR0009	1	Pza	Amortiguador Telescopio Corolla	119.00	119.00	0.00	0.00	0.00	0.00	119.00	A	123	2350	Bs	Bs
62	AMOR0005	1	Pza	Amortiguador Trasero  O/O // KYB // Toy // KYB // Toy	175.00	175.00	0.00	0.00	0.00	0.00	175.00	A	124	2347	Bs	Bs
63	AMOR0009	1	Pza	Amortiguador Telescopio Corolla	119.00	119.00	0.00	0.00	0.00	0.00	119.00	A	124	2350	Bs	Bs
64	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	125	2383	Bs	Bs
65	p1	1	qqq	camisa tela2	89.00	89.00	15.90	0.00	0.00	0.00	73.10	A	126	2380	Bs	Bs
66	p4	1	qqq	camxxxisa deportiva	90.00	90.00	20.50	0.00	0.00	0.00	69.50	A	126	2383	Bs	Bs
67	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	127	2380	Bs	Bs
68	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	127	2383	Bs	Bs
69	p3	2	qqq	xxx	76.00	152.00	0.00	0.00	0.00	0.00	152.00	A	128	2382	Bs	Bs
70	p3	7	qqq	xxx	76.00	532.00	0.00	0.00	0.00	0.00	532.00	V	129	\N	Bs	Bs
71	p3	2	qqq	xxx	76.00	152.00	0.00	0.00	0.00	0.00	152.00	A	130	2382	Bs	Bs
72	p4	5	qqq	camxxxisa deportiva	90.00	450.00	0.00	0.00	0.00	0.00	450.00	A	130	2383	Bs	Bs
73	p4	10	qqq	camxxxisa deportiva	90.00	900.00	0.00	0.00	0.00	0.00	900.00	A	133	2383	Bs	Bs
74	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	134	2383	Bs	Bs
75	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	134	2380	Bs	Bs
76	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	135	2383	Bs	Bs
77	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	136	2383	Bs	Bs
78	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	137	2380	Bs	Bs
79	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	137	2383	Bs	Bs
80	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	138	2380	Bs	Bs
81	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	138	2383	Bs	Bs
82	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	139	2380	Bs	Bs
83	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	139	2383	Bs	Bs
84	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	140	2380	Bs	Bs
85	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	140	2383	Bs	Bs
86	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	141	2380	Bs	Bs
87	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	141	2383	Bs	Bs
88	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	142	2380	Bs	Bs
89	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	142	2383	Bs	Bs
90	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	143	2380	Bs	Bs
91	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	143	2383	Bs	Bs
92	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	144	2380	Bs	Bs
93	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	145	2383	Bs	Bs
94	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	145	2380	Bs	Bs
95	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	146	2383	Bs	Bs
96	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	146	2380	Bs	Bs
97	p4	1	qqq	camxxxisa deportiva	90.00	90.00	0.00	0.00	0.00	0.00	90.00	A	147	2383	Bs	Bs
98	p1	1	qqq	camisa tela2	89.00	89.00	0.00	0.00	0.00	0.00	89.00	A	147	2380	Bs	Bs
\.


--
-- Name: compras_detallecompra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('compras_detallecompra_id_seq', 98, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2015-08-21 17:53:28.957661-04	1	nose	1		9	1
2	2015-08-28 06:31:25.553291-04	5	jejeje	2	Modificado/a texto2.	9	1
3	2015-08-28 06:37:44.901739-04	6	fgfdghdfg	1		9	1
4	2015-09-23 17:12:21.624956-04	2	jose	1		4	1
5	2015-09-25 17:25:57.822872-04	100	Eclipse	3		9	1
6	2015-09-25 17:25:57.901615-04	97	Java	3		9	1
7	2015-09-25 17:25:57.923658-04	94	kjhjh	3		9	1
8	2015-09-25 17:25:57.946038-04	93	iuyiuy	3		9	1
9	2015-09-25 17:25:57.968242-04	91	hg	3		9	1
10	2015-09-25 17:25:57.990273-04	90	jhjh	3		9	1
11	2015-09-25 17:25:58.012557-04	89	hghg	3		9	1
12	2015-09-25 17:25:58.0347-04	88	fsdf	3		9	1
13	2015-09-25 17:25:58.057051-04	86	ghghgh|hghhg|hg|	3		9	1
14	2015-09-25 17:25:58.079015-04	85	ghgh	3		9	1
15	2015-09-25 17:25:58.101596-04	84	nhgh	3		9	1
16	2015-09-25 17:25:58.123652-04	83	jjhjh	3		9	1
17	2015-09-25 17:25:58.145898-04	82	jhj	3		9	1
18	2015-09-25 17:25:58.168009-04	81	jgj	3		9	1
19	2015-09-25 17:27:26.637472-04	110	IntelliJ	3		9	1
20	2015-09-25 17:27:26.672643-04	109	PyCharm	3		9	1
21	2015-09-25 17:27:26.705963-04	108	Visual Studio	3		9	1
22	2015-09-25 17:27:26.728513-04	107	Eclipse	3		9	1
23	2015-09-25 17:27:26.750699-04	106	C	3		9	1
24	2015-09-25 17:27:26.773018-04	105	C	3		9	1
25	2015-09-25 17:27:26.79497-04	104	Java	3		9	1
26	2015-09-25 18:28:49.721288-04	124	IntelliJ	3		9	1
27	2015-09-25 18:28:49.748754-04	123	PyCharm	3		9	1
28	2015-09-25 18:28:49.771139-04	122	Visual Studio	3		9	1
29	2015-09-25 18:28:49.793525-04	121	Eclipse	3		9	1
30	2015-09-25 18:28:49.815267-04	120	C	3		9	1
31	2015-09-25 18:28:49.837712-04	119	C	3		9	1
32	2015-09-25 18:28:49.85985-04	118	Java	3		9	1
33	2015-09-25 18:28:49.893522-04	117	IntelliJ	3		9	1
34	2015-09-25 18:28:49.926717-04	116	PyCharm	3		9	1
35	2015-09-25 18:28:49.960036-04	115	Visual Studio	3		9	1
36	2015-09-25 18:28:49.981969-04	114	Eclipse	3		9	1
37	2015-09-25 18:28:50.004192-04	113	C	3		9	1
38	2015-09-25 18:28:50.026375-04	112	Chatarraaaaaa	3		9	1
39	2015-09-25 18:28:50.049078-04	111	Java	3		9	1
40	2015-09-25 18:31:56.479886-04	13	camisa tela	3		11	1
41	2015-09-25 18:32:28.400409-04	127	juan	3		9	1
42	2015-09-26 11:43:27.425385-04	131	anita	3		9	1
43	2015-09-26 11:43:27.528959-04	130	nancy	3		9	1
44	2015-09-26 11:43:27.540293-04	129	nose	3		9	1
45	2015-09-26 11:43:27.551108-04	128	ramon	3		9	1
46	2015-09-26 11:43:27.562239-04	126	jose	3		9	1
47	2015-09-26 11:43:27.573603-04	125	pedro	3		9	1
48	2015-11-04 12:54:59.775764-04	2	rtete	1		14	1
49	2015-11-04 12:55:10.581336-04	2	rtete	3		14	1
50	2015-11-04 12:56:50.606438-04	3	weewrwe	1		14	1
51	2015-11-04 18:36:16.23763-04	1	 7676- 87878	3		13	1
52	2015-11-05 00:28:39.016277-04	3	 3333- 33333	3		13	1
53	2015-11-05 00:28:39.031676-04	2	 2342- 2234	3		13	1
54	2015-11-05 01:12:27.834951-04	22	 89- 123	3		13	1
55	2015-11-05 01:12:27.866053-04	20	 222- 33343	3		13	1
56	2015-11-05 01:12:27.876796-04	17	 976- 333	3		13	1
57	2015-11-05 01:12:27.888355-04	15	 444- 555	3		13	1
58	2015-11-05 01:12:27.899279-04	13	 6767- 464564	3		13	1
59	2015-11-05 01:12:27.910292-04	11	 23423- 234234	3		13	1
60	2015-11-05 01:12:27.921658-04	8	 24234234- 2423424	3		13	1
61	2015-11-05 01:12:27.93267-04	7	 2323- 1313	3		13	1
62	2015-11-05 01:12:27.943765-04	5	 546- 32323	3		13	1
63	2015-11-05 01:20:09.202846-04	4	ewerw	1		14	1
64	2015-11-05 01:20:17.238844-04	4	ewerw	3		14	1
65	2015-11-05 01:44:36.129515-04	28	 324- 23424	3		13	1
66	2015-11-05 01:44:36.158181-04	26	 342- 3424	3		13	1
67	2015-11-05 01:44:36.169298-04	25	 3444- 333	3		13	1
68	2015-11-05 01:44:36.180421-04	23	 324- 233	3		13	1
69	2015-11-05 01:54:51.340163-04	35	 223- 333	3		13	1
70	2015-11-05 01:54:51.352507-04	33	 323- 455	3		13	1
71	2015-11-05 01:54:51.36378-04	31	 6767- 455	3		13	1
72	2015-11-05 01:54:51.375029-04	29	 324- 23424	3		13	1
73	2015-11-05 02:12:48.076057-04	40	 334- 34344	3		13	1
74	2015-11-05 02:12:48.090844-04	39	 34434- 2222	3		13	1
75	2015-11-05 02:12:48.102052-04	38	 44545- 445	3		13	1
76	2015-11-05 02:12:48.113017-04	37	 344- 34444	3		13	1
77	2015-11-05 02:12:48.124246-04	36	 223- 333	3		13	1
78	2015-11-05 02:28:08.777602-04	45	 334- 3535	3		13	1
79	2015-11-05 02:28:08.7918-04	44	 344- 23424	3		13	1
80	2015-11-05 02:28:08.80293-04	43	 355- 3233	3		13	1
81	2015-11-05 02:28:08.813859-04	42	 633- 545	3		13	1
82	2015-11-05 02:28:08.825237-04	41	 23- 2313	3		13	1
83	2015-11-05 02:44:05.600962-04	49	 324- 2333	3		13	1
84	2015-11-05 02:44:05.62089-04	47	 455- 456	3		13	1
85	2015-11-05 02:44:05.631903-04	46	 344- 333	3		13	1
86	2015-11-05 03:23:21.108783-04	57	 908- 876	3		13	1
87	2015-11-05 03:23:21.128269-04	55	 3245- 566	3		13	1
88	2015-11-05 03:23:21.13938-04	54	 6789- 67895	3		13	1
89	2015-11-05 03:23:21.150684-04	53	 12345- 4321	3		13	1
90	2015-11-05 03:23:21.16174-04	52	 48- 43	3		13	1
91	2015-11-05 03:23:21.172748-04	51	 53- 56	3		13	1
92	2015-11-05 03:23:21.183884-04	50	 343- 44	3		13	1
93	2015-11-05 03:37:49.295679-04	72	 24424- 366	3		13	1
94	2015-11-05 03:37:49.313-04	70	 234- 32424	3		13	1
95	2015-11-05 03:37:49.324104-04	69	 233- 4242	3		13	1
96	2015-11-05 05:37:50.921288-04	83	 4244- 7757	3		13	1
97	2015-11-05 05:37:50.933448-04	82	 233424- 3242	3		13	1
98	2015-11-05 05:37:50.944523-04	81	 646- 899	3		13	1
99	2015-11-05 05:37:50.955743-04	80	 35345- 43535	3		13	1
100	2015-11-05 05:37:50.966893-04	79	 43434- 4535	3		13	1
101	2015-11-05 05:37:50.977935-04	78	 2424- 66333	3		13	1
102	2015-11-05 05:37:50.989086-04	77	 4567- 5666	3		13	1
103	2015-11-05 05:37:51.000093-04	75	 345345- 4242	3		13	1
104	2015-11-05 05:37:51.011396-04	74	 244244- 23424	3		13	1
105	2015-11-05 05:37:51.022473-04	73	 24424- 366	3		13	1
106	2015-11-05 13:37:53.037557-04	91	 4555- 4555	3		13	1
107	2015-11-05 13:37:53.060253-04	87	 9866- 23424	3		13	1
108	2015-11-05 13:37:53.071275-04	86	 45353- 4353453	3		13	1
109	2015-11-05 13:37:53.082099-04	85	 98434- 21414	3		13	1
110	2015-11-06 14:33:33.22685-04	1	 422- ssddd	3		15	1
111	2015-11-06 14:53:31.01651-04	5	 55454- adada	3		15	1
112	2015-11-06 14:53:31.039181-04	3	 53788- venta jejeje	3		15	1
113	2015-11-06 14:53:31.083837-04	2	 45678- ventas de productos	3		15	1
114	2015-11-06 14:53:52.871568-04	7	 33354252- nosee	3		15	1
115	2015-11-09 13:47:51.003236-04	324	Anilla 4JB1-4JA1 93mm 2*2*4 	3		11	1
116	2015-11-09 13:47:51.113049-04	323	Anilla 4JB1-4JA1 93mm 2*2*4 	3		11	1
117	2015-11-09 13:47:51.12447-04	322	Anilla 4ZD1 89,3mm 1,5*1,5*4 	3		11	1
118	2015-11-09 13:47:51.135249-04	321	Anilla P13-H22 87mm  2*1.2*2.8	3		11	1
119	2015-11-09 13:47:51.14655-04	320	Anilla J08C 114mm 2,5*2*4	3		11	1
120	2015-11-09 13:47:51.157497-04	319	Anilla CD 70mm 1.5*1*2.8	3		11	1
121	2015-11-09 13:47:51.168794-04	318	Anilla K3 72mm 1.2*1*2	3		11	1
122	2015-11-09 13:47:51.18056-04	317	Anilla K3 72mm 1.2*1*2	3		11	1
123	2015-11-09 13:47:51.19115-04	316	Anilla Daewo F6-YSE-3EA 68mm 1.2*1.5*2.8	3		11	1
124	2015-11-09 13:47:51.20237-04	315	Amortiguador Telescopio Corolla	3		11	1
125	2015-11-09 13:47:51.214055-04	314	Amortiguador Direccion Mazda M/OM // TOKICO // Maz // TOKICO // Maz	3		11	1
126	2015-11-09 13:47:51.224402-04	313	Amortiguador Direccion Lan Cruiser M/P // KYB // Toy // KYB // Toy	3		11	1
127	2015-11-09 13:47:51.235485-04	312	Amortiguador Trasero  O/O // KYB // Toy // KYB // Toy	3		11	1
128	2015-11-09 13:47:51.247056-04	311	Amortiguador Trasero Ipsum P/O // KYB // Toy // KYB // Toy	3		11	1
129	2015-11-09 13:47:51.257599-04	310	Amortiguador Trasero  Isuzu P/OM // KYB // Isu // KYB // Isu	3		11	1
130	2015-11-09 13:47:51.269212-04	309	Amortiguador  Delantero Patrol P/P // KYB // Nis // KYB // Nis	3		11	1
131	2015-11-09 13:47:51.280256-04	308	Ajustador de correa alternador	3		11	1
132	2015-11-09 13:47:51.291235-04	307	Abrazadera metalica	3		11	1
133	2015-11-09 13:47:51.302222-04	306	Abrasadera de Cremallera	3		11	1
134	2015-11-14 22:44:51.745155-04	2371	camxxxisa deportiva	3		11	1
135	2015-11-14 22:44:51.856592-04	2370	xxx	3		11	1
136	2015-11-14 22:44:51.867684-04	2369	pantalon tela2	3		11	1
137	2015-11-14 22:44:51.878469-04	2368	camisa tela2	3		11	1
138	2015-11-14 22:57:31.034742-04	2375	camxxxisa deportiva	3		11	1
139	2015-11-14 22:57:31.059808-04	2374	xxx	3		11	1
140	2015-11-14 22:57:31.071252-04	2373	pantalon tela2	3		11	1
141	2015-11-14 22:57:31.08205-04	2372	camisa tela2	3		11	1
142	2015-11-16 11:18:56.931176-04	116	 5643- 986	3		13	1
143	2015-11-16 11:18:57.008913-04	115	 678- 9876	3		13	1
144	2015-11-16 11:18:57.020411-04	113	 123- 343	3		13	1
145	2015-11-16 11:18:57.031439-04	112	 545- 656767	3		13	1
146	2015-11-16 11:18:57.042268-04	111	 4545- 5656	3		13	1
147	2015-11-16 11:18:57.05393-04	110	 455- 343242334	3		13	1
148	2015-11-16 11:18:57.064911-04	107	 434- 24234	3		13	1
149	2015-11-16 11:18:57.07538-04	105	 568888888- 4646464	3		13	1
150	2015-11-16 11:18:57.087408-04	104	 687686- 686876	3		13	1
151	2015-11-16 11:18:57.097913-04	93	 2342- 3453535	3		13	1
152	2015-11-16 11:18:57.109117-04	92	 4533- 345345	3		13	1
153	2015-11-24 12:52:45.330741-04	112	 6767- gfgf	3		15	1
154	2015-11-24 12:52:45.430942-04	111	 565- ffgf	3		15	1
155	2015-11-24 12:52:45.441867-04	110	 676- grgf	3		15	1
156	2015-11-24 12:52:45.453069-04	109	 757- ughgg	3		15	1
157	2015-11-24 12:52:45.464358-04	108	 4353- hgghg	3		15	1
158	2015-11-24 12:52:45.475252-04	107	 56- hghgh	3		15	1
159	2015-11-24 12:52:45.486634-04	106	 446- gfgf	3		15	1
160	2015-11-24 12:52:45.497527-04	105	 64646- jhgh	3		15	1
161	2015-11-24 12:52:45.508831-04	104	 787- hhg	3		15	1
162	2015-11-24 12:52:45.520087-04	103	 4646464- ghhg	3		15	1
163	2015-11-24 12:52:45.530898-04	102	 3434- jhj	3		15	1
164	2015-11-24 12:52:45.541904-04	101	 435345- hhgg	3		15	1
165	2015-11-24 12:52:45.553182-04	100	 5656- hgg	3		15	1
166	2015-11-24 12:52:45.564335-04	99	 5656- hgg	3		15	1
167	2015-11-24 12:52:45.575704-04	98	 4535- jhjh	3		15	1
168	2015-11-24 12:52:45.586501-04	97	 565- hghgh	3		15	1
169	2015-11-24 12:52:45.597594-04	96	 3453- hghg	3		15	1
170	2015-11-24 12:52:45.60844-04	95	 979- sfdfs	3		15	1
171	2015-11-24 12:52:45.619963-04	94	 34224- fdfsdf	3		15	1
172	2015-11-24 12:52:45.630873-04	93	 34546- sttfdg	3		15	1
173	2015-11-24 12:52:45.642168-04	92	 676- ghhg	3		15	1
174	2015-11-24 12:52:45.653371-04	91	 3453- jhjh	3		15	1
175	2015-11-24 12:52:45.664393-04	90	 65655- jhgg	3		15	1
176	2015-11-24 12:52:45.675485-04	89	 34534- jhjg	3		15	1
177	2015-11-24 12:52:45.686674-04	88	 32423- hghg	3		15	1
178	2015-11-24 12:52:45.697437-04	87	 333- bhghg	3		15	1
179	2015-11-24 12:52:45.709347-04	86	 324- kjhj	3		15	1
180	2015-11-24 12:52:45.719989-04	85	 23234- jhjh	3		15	1
181	2015-11-24 12:52:45.730931-04	84	 345345- sdfsdf	3		15	1
182	2015-11-24 12:52:45.742208-04	83	 3434- sdfsdf	3		15	1
183	2015-11-24 12:52:45.75342-04	82	 322- dsfs	3		15	1
184	2015-11-24 12:52:45.764575-04	81	 3232- jhjhj	3		15	1
185	2015-11-24 12:52:45.775625-04	80	 3453- retert|	3		15	1
186	2015-11-24 12:52:45.78662-04	79	 5555- dfgd	3		15	1
187	2015-11-24 12:52:45.797552-04	78	 23234- hghghg	3		15	1
188	2015-11-24 12:52:45.808835-04	77	 345345- terte	3		15	1
189	2015-11-24 12:52:45.819932-04	76	 435345- mhjh	3		15	1
190	2015-11-24 12:52:45.831051-04	75	 3434- hgh	3		15	1
191	2015-11-24 12:52:45.842014-04	74	 324234- dsfdf	3		15	1
192	2015-11-24 12:52:45.852986-04	73	 23234- hghhg	3		15	1
193	2015-11-24 12:52:45.864638-04	72	 234234- nbnb	3		15	1
194	2015-11-24 12:52:45.875459-04	71	 343242- srer	3		15	1
195	2015-11-24 12:52:45.886593-04	70	 344353- dfggfh	3		15	1
196	2015-11-24 12:52:45.8979-04	69	 2324- hghg	3		15	1
197	2015-11-24 12:52:45.908923-04	68	 324234- qweqwe	3		15	1
198	2015-11-24 12:52:45.920135-04	67	 324234- werwer	3		15	1
199	2015-11-24 12:52:45.931258-04	66	 324234- werwer	3		15	1
200	2015-11-24 12:52:45.942207-04	65	 234234- ewrwer	3		15	1
201	2015-11-24 12:52:45.953312-04	64	 234324- werwerw	3		15	1
202	2015-11-24 12:52:45.96448-04	63	 5656- LKKL	3		15	1
203	2015-11-24 12:52:45.975283-04	62	 3423- sdfsd	3		15	1
204	2015-11-24 12:52:45.986477-04	61	 0- asdasd	3		15	1
205	2015-11-24 12:52:45.997697-04	60	 342- qeqe	3		15	1
206	2015-11-24 12:52:46.008617-04	59	 345- sddasd	3		15	1
207	2015-11-24 12:52:46.020135-04	58	 345- adad	3		15	1
208	2015-11-24 12:52:46.031332-04	57	 0- zxczc	3		15	1
209	2015-11-24 12:52:46.042204-04	55	 4- asdasd	3		15	1
210	2015-11-24 12:52:46.053508-04	50	 0- zcz	3		15	1
211	2015-11-24 12:52:46.064501-04	49	 12312- asaas	3		15	1
212	2015-11-24 12:52:46.075851-04	48	 645- asdada	3		15	1
213	2015-11-24 12:52:46.086792-04	47	 45563- dfdfdf	3		15	1
214	2015-11-24 12:52:46.097698-04	45	 345- dfffff	3		15	1
215	2015-11-24 12:52:46.109148-04	43	 5076- adad	3		15	1
216	2015-11-24 12:52:46.120027-04	42	 5607- vetasssssss	3		15	1
217	2015-11-24 12:52:46.131195-04	41	 7089- ventitas	3		15	1
218	2015-11-24 12:52:46.14245-04	40	 2232- ssddd	3		15	1
219	2015-11-24 12:52:46.15344-04	39	 5684- sdfsdf	3		15	1
220	2015-11-24 12:52:46.164614-04	38	 66789- asdasd	3		15	1
221	2015-11-24 12:52:46.175727-04	36	 32323- sdfsfs	3		15	1
222	2015-11-24 12:52:46.186916-04	35	 1234- adadad	3		15	1
223	2015-11-24 12:52:46.197833-04	34	 43434- erwrw	3		15	1
224	2015-11-24 12:52:46.209152-04	31	 6788- sfsfs	3		15	1
225	2015-11-24 12:52:46.219959-04	30	 4789- tetet	3		15	1
226	2015-11-24 12:52:46.231404-04	29	 9087- reererer	3		15	1
227	2015-11-24 12:52:46.242659-04	27	 4535- adadad	3		15	1
228	2015-11-24 12:52:46.253375-04	26	 212- asdad	3		15	1
229	2015-11-24 12:52:46.26491-04	25	 9377- terr	3		15	1
230	2015-11-24 12:52:46.275803-04	24	 45533- wrwr	3		15	1
231	2015-11-24 12:52:46.286777-04	23	 43535- rwrwr	3		15	1
232	2015-11-24 12:52:46.297829-04	22	 6789- fafa	3		15	1
233	2015-11-24 12:52:46.308987-04	21	 45678- ferefe	3		15	1
234	2015-11-24 12:52:46.320053-04	20	 4567- asdad	3		15	1
235	2015-11-24 12:52:46.331464-04	19	 4343- dsgs	3		15	1
236	2015-11-24 12:52:46.342342-04	18	 33333- kjkjk	3		15	1
237	2015-11-24 12:52:46.353539-04	17	 211313- sada	3		15	1
238	2015-11-24 12:52:46.364819-04	16	 453555- asdasdasd	3		15	1
239	2015-11-24 12:52:46.375605-04	15	 32424- ff	3		15	1
240	2015-11-24 12:52:46.386763-04	13	 2342424- dggd	3		15	1
241	2015-11-24 12:52:46.397888-04	12	 3234324- werwerwe	3		15	1
242	2015-11-24 12:52:46.408935-04	11	 4344- sdfdsfsf	3		15	1
243	2015-11-24 12:52:46.420506-04	10	 567787- venta1	3		15	1
244	2015-11-24 12:53:34.108526-04	2380	p1-camisa tela2	2	Modificado/a cantidad.	11	1
245	2015-11-24 12:53:47.435362-04	2383	p4-camxxxisa deportiva	2	Modificado/a cantidad.	11	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 245, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	inicio	libro
8	captcha	captchastore
9	proveedores	proveedor
10	almacenes	item
11	producto	item
12	cliente	cliente
13	compras	compra
14	compras	detallecompra
15	ventas	venta
16	ventas	detalleventa
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_content_type_id_seq', 16, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2015-08-18 17:58:18.966153-04
2	auth	0001_initial	2015-08-18 17:58:20.132243-04
3	admin	0001_initial	2015-08-18 17:58:20.387655-04
4	contenttypes	0002_remove_content_type_name	2015-08-18 17:58:20.498368-04
5	auth	0002_alter_permission_name_max_length	2015-08-18 17:58:20.542824-04
6	auth	0003_alter_user_email_max_length	2015-08-18 17:58:20.598056-04
7	auth	0004_alter_user_username_opts	2015-08-18 17:58:20.643915-04
8	auth	0005_alter_user_last_login_null	2015-08-18 17:58:20.698164-04
9	auth	0006_require_contenttypes_0002	2015-08-18 17:58:20.709975-04
10	sessions	0001_initial	2015-08-18 17:58:20.920966-04
11	inicio	0001_initial	2015-08-18 18:55:55.230095-04
12	inicio	0002_auto_20150818_2254	2015-08-18 18:55:55.257599-04
13	inicio	0003_delete_libro	2015-08-18 19:01:39.528562-04
14	captcha	0001_initial	2015-08-19 17:25:32.695686-04
15	captcha	0002_delete_captchastore	2015-08-21 17:49:37.433542-04
16	proveedores	0001_initial	2015-08-21 17:49:37.795392-04
17	almacenes	0001_initial	2015-08-29 11:11:41.440941-04
18	producto	0001_initial	2015-09-18 20:56:36.389828-04
19	producto	0002_auto_20150919_0056	2015-09-18 20:56:36.609079-04
20	cliente	0001_initial	2015-09-19 13:49:35.956938-04
21	proveedores	0002_auto_20150923_1625	2015-09-23 12:25:30.893318-04
22	proveedores	0003_auto_20150923_2059	2015-09-23 16:59:26.040635-04
23	cliente	0002_cliente_user	2015-09-23 17:13:02.351162-04
24	proveedores	0004_proveedor_user	2015-09-23 17:14:38.346645-04
25	producto	0003_item_user	2015-09-23 17:30:23.476351-04
26	producto	0004_auto_20150925_2225	2015-09-25 18:26:00.688921-04
27	proveedores	0005_auto_20150925_2225	2015-09-25 18:26:00.841541-04
28	producto	0005_auto_20150926_1535	2015-09-26 11:36:00.854582-04
29	producto	0006_auto_20150926_1548	2015-09-26 11:48:31.207068-04
30	compras	0001_initial	2015-10-12 13:09:35.340909-04
31	compras	0002_auto_20151104_1656	2015-11-04 12:56:14.121896-04
32	compras	0003_auto_20151104_2034	2015-11-04 16:34:22.676942-04
33	compras	0004_auto_20151104_2147	2015-11-04 17:47:43.191945-04
34	compras	0005_auto_20151105_0527	2015-11-05 01:27:27.763414-04
35	compras	0006_auto_20151105_0544	2015-11-05 01:44:18.386565-04
36	compras	0007_auto_20151105_0551	2015-11-05 01:52:00.531393-04
37	compras	0008_auto_20151105_0642	2015-11-05 02:42:34.50529-04
38	producto	0007_auto_20151105_0642	2015-11-05 02:42:35.172319-04
39	compras	0009_auto_20151105_0936	2015-11-05 05:37:04.078663-04
40	ventas	0001_initial	2015-11-06 14:07:15.742823-04
41	ventas	0002_auto_20151106_1859	2015-11-06 14:59:54.089737-04
42	producto	0008_auto_20151107_1730	2015-11-07 13:30:59.685938-04
43	producto	0009_auto_20151107_2015	2015-11-07 16:16:04.455912-04
44	compras	0010_auto_20151116_1355	2015-11-16 09:55:35.77104-04
45	ventas	0003_auto_20151116_2313	2015-11-16 19:13:50.563302-04
46	compras	0011_auto_20151116_2341	2015-11-16 19:41:27.426515-04
47	ventas	0004_auto_20151116_2359	2015-11-16 19:59:25.944227-04
48	cliente	0002_auto_20151116_1435	2015-11-16 20:47:43.80343-04
49	cliente	0003_remove_cliente_user	2015-11-16 20:47:43.986357-04
50	cliente	0004_auto_20151116_1957	2015-11-16 20:47:44.029868-04
51	cliente	0005_auto_20151116_2002	2015-11-16 20:47:44.064206-04
52	cliente	0006_auto_20151116_2005	2015-11-16 20:47:44.096508-04
53	compras	0012_auto_20151117_1413	2015-11-17 10:13:24.26225-04
54	ventas	0005_auto_20151117_1413	2015-11-17 10:13:25.382061-04
55	cliente	0002_auto_20151118_1312	2015-11-18 09:12:35.800105-04
56	cliente	0003_auto_20151118_1404	2015-11-18 10:05:27.0681-04
57	cliente	0002_auto_20151118_1457	2015-11-18 10:57:24.589165-04
58	cliente	0002_auto_20151118_1611	2015-11-18 12:11:46.081857-04
59	producto	0010_auto_20151119_2133	2015-11-19 17:33:44.257231-04
60	producto	0011_auto_20151119_2140	2015-11-19 17:40:14.091855-04
61	compras	0013_auto_20151127_2214	2015-11-27 18:39:54.418879-04
62	compras	0014_auto_20151127_2219	2015-11-27 18:39:54.732002-04
63	compras	0015_auto_20151127_2239	2015-11-27 18:39:54.909764-04
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_migrations_id_seq', 63, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: root
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
qxcehz5pgj9t5a7q167xjsdnn4ao3o8l	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-09 16:38:47.013838-04
go5g5cuy6t8u43ftsb4bdeaev8iw61zm	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-10 10:20:51.812383-04
qdm4a0yd43sjfpb4pa4nn20eyy5aw80p	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-16 00:55:28.428608-04
bwnlttul6g5c56xo22s3nnfew09zj2l9	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-16 10:27:41.173455-04
67nmaj69zx8yu8q4yc2jml531a75zn6d	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-19 13:50:39.166644-04
sqengy1xhom3rfp8qdg4ltei4bbzbtf8	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-20 11:17:16.58056-04
sr7j9xqctqdljrynlmayu6s5qhmxihq3	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-09-04 17:52:03.367575-04
1hamz54b2n9j5n2geb92148colnhen89	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-09-11 05:15:22.342461-04
goaxeiqo98cuktefdtabsufscogphg0n	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-21 15:05:47.639607-04
elzaeuq89mr1acchk9vb60enik3xsv75	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-09-11 15:16:08.359496-04
1n0yhc2vubus65kyo1g32a1sfvs7kb0e	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-22 15:47:17.750042-04
63gaz5ebpkjdu2xoh2ufryt4t8ueow38	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-26 10:59:44.292876-04
im0av0c5ei1oty020bawd62549gtucmg	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-26 11:02:14.721751-04
xcstr7ai8fhx6w26gdrv5hkqenafvoa1	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-03 13:50:40.045017-04
mw2t9tohr8m2tkm88zfq9onj7w7yid0t	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-26 13:21:37.91897-04
0tfvmu9aytad89vl0g0otbes70tnjndu	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-05 12:35:29.404678-04
oa75ujrjuu1np5ebvx40thefimzceg49	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-05 14:09:27.194853-04
47u8buimacmd1iscihn4poehkorn4ot4	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-29 17:49:18.578151-04
wctqfses1sugu8c3oym0c6r8jvu8rd0b	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-30 16:33:51.210039-04
nkn5feaqhq0i126bm2ed3yg8hrkagxwd	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-06 15:23:28.799136-04
arwxc4gt1kfdlkqulbirl7mbkmsvhcf4	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-07 11:23:58.548938-04
vma9q48lkscve2ej9fimuyuh5z70wjcf	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-10-07 12:20:50.217474-04
bwf9gtgje8zkjlfcojeueblvkfqdbc20	YmUyNzUyNDk4YmE0OGNmOTMwMTQ2Njk0MTBjMjBjODFmMmZiMTNiYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjI3OTQ5NDgzMWE0YzQ0Mzk5MTAzZTY2Nzg4NzIyNjdiMDk3YTY4ZGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=	2015-10-07 19:23:38.636261-04
qxybmccp5zl2gdnp9bevlz99uub26zp5	YmUyNzUyNDk4YmE0OGNmOTMwMTQ2Njk0MTBjMjBjODFmMmZiMTNiYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjI3OTQ5NDgzMWE0YzQ0Mzk5MTAzZTY2Nzg4NzIyNjdiMDk3YTY4ZGMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=	2015-10-08 19:44:02.351391-04
hr57ndjrv708wagah4px9v65sfhh5iex	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-11-06 12:02:10.076543-04
1dmqtbbksy05npin9l5flutnavb4lwej	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-11-17 11:59:34.123064-04
3ji5mt2nv8gq65c7e40xmugjtojmuord	NDIxYzZjMWRjZmFiMzRhMmY5N2Q4NmQ1YWJlZDdkZTE2NGYxMGFhZDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2015-11-21 14:08:56.104471-04
jqa1x1n9izwwidjixukmditv2lwlca2t	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-12-02 15:11:39.681001-04
pqmxkuetbeoczdkxpgw228swv7b4innb	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-12-04 12:19:10.110797-04
i88ueymh34pmrrg3297e4wwo9zxvlggx	YzUxOWJjYmVjYjAwZDlmMTZlMTM1MWI5NTg2Y2EyZGE5ZmRmNzIwNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZmE5Y2U3NmE2ZDJiMGI1ZDJkMmE3ZmU0NTIzOTYzODBiYzBlZWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-12-17 17:50:20.706698-04
\.


--
-- Data for Name: producto_item; Type: TABLE DATA; Schema: public; Owner: root
--

COPY producto_item (id, codigo_item, codigo_fabrica, almacen, grupo, subgrupo, descripcion, carac_especial_1, carac_especial_2, cantidad, saldo_min, imagen, unidad_medida, costo_unitario, precio_unitario, proveedor_id, user_id) FROM stdin;
2381	p2	aa	2	g1	sss	pantalon tela2	aaa	qqq	12	5	ggg	qqq	34.00	89.00	172	1
2341	ABRA0027	45517-12111-T	1	UNIVERSAL	Abrazadera	Abrasadera de Cremallera	0.0	TAIWAN	17	1		Pza	8.35	50.00	170	1
2351	ANIL0001	12140-78B00-STD	1	DAEWO	Anilla	Anilla Daewo F6-YSE-3EA 68mm 1.2*1.5*2.8	SWD-20002ZZ-STD	NPR	2	1		Pza	45.94	231.00	170	1
2352	ANIL0002	13011-97401-STD-P	1	SUZUKI	Anilla	Anilla K3 72mm 1.2*1*2	31049/STD	TP	2	1		Pza	50.11	252.00	170	1
2353	ANIL0003	13011-97401-0.25-P	1	SUZUKI	Anilla	Anilla K3 72mm 1.2*1*2	31049/0.25	TP	2	1		Pza	50.11	252.00	170	1
2354	ANIL0004	13011-87712-STD-P	1	DAIHATSU	Anilla	Anilla CD 70mm 1.5*1*2.8	31027/STD	TP	1	1		Pza	50.11	252.00	170	1
2355	ANIL0008	13011-3570A-STD-P	1	HINO	Anilla	Anilla J08C 114mm 2,5*2*4	32263/STD	TP	7	1		Pza	264.48	1330.00	170	1
2349	AMOR0008	SD1009	1	MAZDA	Amortiguador	Amortiguador Direccion Mazda M/OM // TOKICO // Maz // TOKICO // Maz	0.0	TOKICO	3	1		Pza	89.09	448.00	170	1
2346	AMOR0004	444153.0	1	TOYOTA	Amortiguador	Amortiguador Trasero Ipsum P/O // KYB // Toy // KYB // Toy	0.0	YOKOMITSU	4	1		Pza	37.58	189.00	170	1
2348	AMOR0007	KS1005	1	TOYOTA	Amortiguador	Amortiguador Direccion Lan Cruiser M/P // KYB // Toy // KYB // Toy	0.0	KYB	5	1		Pza	89.09	448.00	170	1
2344	AMOR0002	444159.0	1	NISSAN	Amortiguador	Amortiguador  Delantero Patrol P/P // KYB // Nis // KYB // Nis	0.0	KYB	5	1		Pza	44.54	224.00	170	1
2345	AMOR0003	444213.0	1	TOYOTA	Amortiguador	Amortiguador Trasero  Isuzu P/OM // KYB // Isu // KYB // Isu	0.0	YOKOMITSU	5	1		Pza	23.66	119.00	170	1
2347	AMOR0005	444023.0	1	TOYOTA	Amortiguador	Amortiguador Trasero  O/O // KYB // Toy // KYB // Toy	0.0	KYB	13	1		Pza	34.80	175.00	170	1
2350	AMOR0009	S3073	1	TOYOTA	Amortiguador	Amortiguador Telescopio Corolla	0.0	YOKOMITSU	10	1		Pza	23.66	119.00	170	1
2384	imagen	asass	1	asas	g	asas	hghg	assa	3	4		mtros	1545.00	45.50	170	1
2385	producto	gf	21	gf	kkj	gfg	kjk	gfgf	565	45		hgh	566.00	56.00	171	1
2383	p4	ss	3	g1	fffffff	camxxxisa deportiva	aaaa	qqq	9	7	ggg	qqq	69.00	90.00	171	1
2380	p1	qq	1	g1	aaaa	camisa tela2	aaa	qqq	39	4	hhhhh	qqq	34.00	89.00	170	1
2382	p3	ww	1	g2	ddd	xxx	aaa	qqq	0	6	ggg	qqq	56.00	76.00	171	1
\.


--
-- Name: producto_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('producto_item_id_seq', 2385, true);


--
-- Data for Name: proveedores_proveedor; Type: TABLE DATA; Schema: public; Owner: root
--

COPY proveedores_proveedor (id, codigo, razon_social, nit, direccion, telefono1, telefono2, telefono3, contactos, rubro, ubicacion_geo, fecha1, fecha2, texto1, texto2, user_id) FROM stdin;
170	p1	pedro	qwqww	hkjhj	45644446	\N	\N	errerere	hjhjh	jhjhh	2015-09-23	2015-09-23	jhjhjhj	jhjh	1
171	p2	jose	uyyyuyuyy	wewe	343434	\N	\N	erer	dfdhdh	ererrrreer	2015-09-23	2015-09-23	uuuuuu	ererer	1
172	p3	juan	ewewe	wewe	343434	\N	\N	erererree	hdhdh	erererre	2015-09-23	2015-09-23	ttttttt	ererer	1
173	p4	ramon	wewew	weewe	343434	\N	\N	ererere	dhdhd	yyyyyy	2015-09-23	2015-09-23	rterrere	ererer	1
174	p5	nose	wewew	wewe	343434	\N	\N	erereerer	dhdhdhdh	uuuuuuu	2015-09-23	2015-09-23	ererreerr	ererewew	1
199	hjhjhj	ghghg	45646	ggrttr	4545454	54544	45445454	rtrtrrt	rtrtr	trt	2015-11-15	2015-11-15	jhghg	\N	1
200	jkjkj	kjkjkj	5675	ytyt	3435646	56565	56565	rttrt	rtrt	trtr	2015-11-15	2015-11-15	jhhhg	\N	1
201	jjhj	jhjh	76676	ytytyt	6566556	\N	\N	ytytty	ytyt	ytyt	2015-11-18	2015-11-18	jjhj	\N	1
\.


--
-- Name: proveedores_proveedor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('proveedores_proveedor_id_seq', 201, true);


--
-- Data for Name: ventas_detalleventa; Type: TABLE DATA; Schema: public; Owner: root
--

COPY ventas_detalleventa (id, cantidad, subtotal, descuento, recargo, ice, excentos, scf, producto_id, venta_id, tipo_descuento, tipo_recargo) FROM stdin;
157	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	114	Bs	Bs
158	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	114	Bs	Bs
159	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	115	Bs	Bs
160	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	115	Bs	Bs
161	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	116	Bs	Bs
162	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	116	Bs	Bs
163	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	117	Bs	Bs
164	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	117	Bs	Bs
165	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	118	Bs	Bs
166	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	118	Bs	Bs
167	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	119	Bs	Bs
168	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	119	Bs	Bs
169	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	120	Bs	Bs
170	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	120	Bs	Bs
171	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	121	Bs	Bs
172	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	121	Bs	Bs
173	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	122	Bs	Bs
174	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	122	Bs	Bs
175	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	123	Bs	Bs
176	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	123	Bs	Bs
177	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	124	Bs	Bs
178	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	124	Bs	Bs
179	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	125	Bs	Bs
180	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	125	Bs	Bs
181	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	126	Bs	Bs
182	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	126	Bs	Bs
183	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	127	Bs	Bs
184	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	127	Bs	Bs
185	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	128	Bs	Bs
186	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	128	Bs	Bs
187	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	129	Bs	Bs
188	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	129	Bs	Bs
189	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	130	Bs	Bs
190	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	130	Bs	Bs
191	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	131	Bs	Bs
192	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	131	Bs	Bs
193	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	132	Bs	Bs
194	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	132	Bs	Bs
195	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	133	Bs	Bs
196	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	133	Bs	Bs
197	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	134	Bs	Bs
198	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	134	Bs	Bs
199	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	135	Bs	Bs
200	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	135	Bs	Bs
201	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	136	Bs	Bs
202	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	136	Bs	Bs
203	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	137	Bs	Bs
204	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	137	Bs	Bs
205	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	138	Bs	Bs
206	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	138	Bs	Bs
207	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	139	Bs	Bs
208	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	139	Bs	Bs
209	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	140	Bs	Bs
210	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	140	Bs	Bs
211	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	141	Bs	Bs
212	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	141	Bs	Bs
213	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	142	Bs	Bs
214	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	142	Bs	Bs
215	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	143	Bs	Bs
216	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	143	Bs	Bs
217	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	144	Bs	Bs
218	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	145	Bs	Bs
219	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	146	Bs	Bs
220	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	147	Bs	Bs
221	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	148	Bs	Bs
222	1	76.00	0.00	0.00	0.00	0.00	76.00	2382	149	Bs	Bs
223	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	149	Bs	Bs
224	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	150	Bs	Bs
225	1	76.00	0.00	0.00	0.00	0.00	76.00	2382	150	Bs	Bs
226	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	151	Bs	Bs
227	1	76.00	0.00	0.00	0.00	0.00	76.00	2382	151	Bs	Bs
228	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	152	Bs	Bs
229	1	76.00	0.00	0.00	0.00	0.00	76.00	2382	152	Bs	Bs
230	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	154	Bs	Bs
231	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	155	Bs	Bs
232	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	156	Bs	Bs
233	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	157	Bs	Bs
234	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	158	Bs	Bs
235	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	159	Bs	Bs
236	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	160	Bs	Bs
237	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	161	Bs	Bs
238	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	162	Bs	Bs
239	1	76.00	0.00	0.00	0.00	0.00	76.00	2382	162	Bs	Bs
240	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	163	Bs	Bs
241	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	163	Bs	Bs
242	2	178.00	0.00	0.00	0.00	0.00	178.00	2380	164	Bs	Bs
243	5	450.00	0.00	0.00	0.00	0.00	450.00	2383	164	Bs	Bs
244	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	165	Bs	Bs
245	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	165	Bs	Bs
246	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	166	Bs	Bs
247	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	166	Bs	Bs
248	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	167	Bs	Bs
249	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	168	Bs	Bs
250	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	168	Bs	Bs
251	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	169	Bs	Bs
252	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	169	Bs	Bs
253	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	170	Bs	Bs
254	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	170	Bs	Bs
255	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	171	Bs	Bs
256	1	89.00	0.00	0.00	0.00	0.00	89.00	2380	171	Bs	Bs
257	1	90.00	0.00	0.00	0.00	0.00	90.00	2383	172	Bs	Bs
258	1	89.00	10.00	0.00	0.00	0.00	79.00	2380	172	Bs	Bs
\.


--
-- Name: ventas_detalleventa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('ventas_detalleventa_id_seq', 258, true);


--
-- Data for Name: ventas_venta; Type: TABLE DATA; Schema: public; Owner: root
--

COPY ventas_venta (id, fecha, nit, razon_social, tipo_compra, cantidad_dias, total) FROM stdin;
113	2015-11-24	5656	hghgh	contado	0	0.00
114	2015-11-24	688	hghggh	contado	0	179.00
115	2015-11-24	409	jhj	contado	0	179.00
116	2015-11-24	566	gfhg	contado	0	179.00
117	2015-11-24	7575	jjhhj	contado	0	179.00
118	2015-11-24	79	ghg	contado	0	179.00
119	2015-11-24	4455	nbb	contado	0	179.00
120	2015-11-24	987	hghg	contado	0	179.00
121	2015-11-24	344	jjh	contado	0	179.00
122	2015-11-24	455	jhjh	contado	0	179.00
123	2015-11-24	5656	ytyt	contado	0	179.00
124	2015-11-24	454	hghg	contado	0	179.00
125	2015-11-24	334	uyu	contado	0	179.00
126	2015-11-24	748	hgh	contado	0	179.00
127	2015-11-24	455	hghg	contado	0	179.00
128	2015-11-24	456	hggh	contado	0	179.00
129	2015-11-24	788	hgh	contado	0	179.00
130	2015-11-24	456	hghg	contado	0	179.00
131	2015-11-24	424	ghg	contado	0	179.00
132	2015-11-24	454	hgghgh	contado	0	179.00
133	2015-11-24	565	jhhj	contado	0	179.00
134	2015-11-24	76	hghg	contado	0	179.00
135	2015-11-24	566	hggh	contado	0	179.00
136	2015-11-24	334	kjhh	contado	0	179.00
137	2015-11-24	676	ghg	contado	0	179.00
138	2015-11-24	7878	gfggf	contado	0	179.00
139	2015-11-24	23234	jhjh	contado	0	179.00
140	2015-11-24	676	ghg	contado	0	179.00
141	2015-11-24	32432	kjkj	contado	0	179.00
142	2015-11-24	667	hghg	contado	0	179.00
143	2015-11-25	87	hgf	contado	0	179.00
144	2015-11-25	34534	jhj	contado	0	90.00
145	2015-11-25	567	hghg	contado	0	90.00
146	2015-11-25	4555	hjh	credito	6	90.00
147	2015-11-25	45454	hghg	contado	0	90.00
148	2015-11-25	748	gfgf	contado	0	90.00
149	2015-11-25	3242	sdfsd	contado	0	165.00
150	2015-11-25	788	hghg	credito	5	165.00
151	2015-11-25	332	jjh	credito	56	165.00
152	2015-11-25	45345	nnn	credito	4	165.00
153	2015-11-27	234234234	werwer	contado	0	0.00
154	2015-11-27	567345435	hghgh	contado	0	89.00
155	2015-11-27	76788	jhhjjh	contado	0	89.00
156	2015-11-27	5787	nghgh	contado	0	89.00
157	2015-11-27	54654	jhhj	contado	0	89.00
158	2015-11-27	464345	hghgh	contado	0	89.00
159	2015-11-27	4677	hgjgjg	contado	0	89.00
160	2015-11-27	45677	jjhj	contado	0	89.00
161	2015-11-27	67676	hgghgh	contado	0	89.00
162	2015-11-27	5788	hhghgh	contado	0	165.00
163	2015-11-27	67833	hjhhh	contado	0	179.00
164	2015-11-27	2799	hghg	contado	0	628.00
165	2015-11-27	3243242	dfgfdgfdg	contado	0	179.00
166	2015-11-30	5098	entel	contado	0	179.00
167	2015-11-30	5098	entel	contado	0	90.00
168	2015-12-02	56565	ytyttyty	contado	0	179.00
169	2015-12-02	45555	safdsfsd	contado	0	179.00
170	2015-12-04	565324	gjg	contado	0	179.00
171	2015-12-04	9858	conteco	contado	0	179.00
172	2015-12-04	5656	hjhjh	contado	0	169.00
\.


--
-- Name: ventas_venta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('ventas_venta_id_seq', 172, true);


--
-- Name: almacenes_item_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY almacenes_item
    ADD CONSTRAINT almacenes_item_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: cliente_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY cliente_cliente
    ADD CONSTRAINT cliente_cliente_pkey PRIMARY KEY (id);


--
-- Name: compras_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY compras_compra
    ADD CONSTRAINT compras_compra_pkey PRIMARY KEY (id);


--
-- Name: compras_detallecompra_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY compras_detallecompra
    ADD CONSTRAINT compras_detallecompra_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: producto_item_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY producto_item
    ADD CONSTRAINT producto_item_pkey PRIMARY KEY (id);


--
-- Name: proveedores_proveedor_codigo_4566124652cfe34a_uniq; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY proveedores_proveedor
    ADD CONSTRAINT proveedores_proveedor_codigo_4566124652cfe34a_uniq UNIQUE (codigo);


--
-- Name: proveedores_proveedor_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY proveedores_proveedor
    ADD CONSTRAINT proveedores_proveedor_pkey PRIMARY KEY (id);


--
-- Name: ventas_detalleventa_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY ventas_detalleventa
    ADD CONSTRAINT ventas_detalleventa_pkey PRIMARY KEY (id);


--
-- Name: ventas_venta_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY ventas_venta
    ADD CONSTRAINT ventas_venta_pkey PRIMARY KEY (id);


--
-- Name: almacenes_item_7ac33b97; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX almacenes_item_7ac33b97 ON almacenes_item USING btree (proveedor_id);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: compras_detallecompra_98926b7a; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX compras_detallecompra_98926b7a ON compras_detallecompra USING btree (compra_id);


--
-- Name: compras_detallecompra_bb91903a; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX compras_detallecompra_bb91903a ON compras_detallecompra USING btree (producto_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: producto_item_7ac33b97; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX producto_item_7ac33b97 ON producto_item USING btree (proveedor_id);


--
-- Name: producto_item_e8701ad4; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX producto_item_e8701ad4 ON producto_item USING btree (user_id);


--
-- Name: proveedores_proveedor_e8701ad4; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX proveedores_proveedor_e8701ad4 ON proveedores_proveedor USING btree (user_id);


--
-- Name: ventas_detalleventa_a3d89257; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX ventas_detalleventa_a3d89257 ON ventas_detalleventa USING btree (venta_id);


--
-- Name: ventas_detalleventa_bb91903a; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE INDEX ventas_detalleventa_bb91903a ON ventas_detalleventa USING btree (producto_id);


--
-- Name: almac_proveedor_id_65c436bdd42a4286_fk_proveedores_proveedor_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY almacenes_item
    ADD CONSTRAINT almac_proveedor_id_65c436bdd42a4286_fk_proveedores_proveedor_id FOREIGN KEY (proveedor_id) REFERENCES proveedores_proveedor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: compras_detall_producto_id_70cc5b8fd5c40dd8_fk_producto_item_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY compras_detallecompra
    ADD CONSTRAINT compras_detall_producto_id_70cc5b8fd5c40dd8_fk_producto_item_id FOREIGN KEY (producto_id) REFERENCES producto_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: compras_detalle_compra_id_260163a87f2dc4c4_fk_compras_compra_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY compras_detallecompra
    ADD CONSTRAINT compras_detalle_compra_id_260163a87f2dc4c4_fk_compras_compra_id FOREIGN KEY (compra_id) REFERENCES compras_compra(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: produ_proveedor_id_2e3a63b725ac1d76_fk_proveedores_proveedor_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY producto_item
    ADD CONSTRAINT produ_proveedor_id_2e3a63b725ac1d76_fk_proveedores_proveedor_id FOREIGN KEY (proveedor_id) REFERENCES proveedores_proveedor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: producto_item_user_id_6d48f690ae37d8e0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY producto_item
    ADD CONSTRAINT producto_item_user_id_6d48f690ae37d8e0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proveedores_proveedor_user_id_228f2e62237ca3ef_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY proveedores_proveedor
    ADD CONSTRAINT proveedores_proveedor_user_id_228f2e62237ca3ef_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ventas_detalle_producto_id_118158844bdb77dc_fk_producto_item_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY ventas_detalleventa
    ADD CONSTRAINT ventas_detalle_producto_id_118158844bdb77dc_fk_producto_item_id FOREIGN KEY (producto_id) REFERENCES producto_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ventas_detallevent_venta_id_40e30ceafe7e4dbd_fk_ventas_venta_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY ventas_detalleventa
    ADD CONSTRAINT ventas_detallevent_venta_id_40e30ceafe7e4dbd_fk_ventas_venta_id FOREIGN KEY (venta_id) REFERENCES ventas_venta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

