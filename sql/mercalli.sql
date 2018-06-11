-- Table: public.mercalli

-- DROP TABLE public.mercalli;

CREATE TABLE public.mercalli
(
  id integer NOT NULL,
  value_txt character varying(10),
  detail_txt character varying(255),
  color_ind character varying(10),
  magnitude_txt character varying(25),
  description_txt character varying,
  CONSTRAINT mercalli_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.mercalli
  OWNER TO "disaster-resilience";

GRANT ALL ON TABLE public."mercalli" TO "disaster-resilience";
GRANT SELECT ON TABLE public."mercalli" TO "disaster-resilience-readonly";
