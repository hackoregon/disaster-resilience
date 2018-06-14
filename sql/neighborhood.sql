-- Table: public.neighborhood

 DROP TABLE public.neighborhood;

CREATE TABLE public.neighborhood
(
  id integer,
  description_txt character varying(255),
  census_response_rate character varying(255),
  quadrant_txt character varying(255),
  CONSTRAINT neighborhood_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.neighborhood
  OWNER TO "disaster-resilience";

GRANT ALL ON TABLE public."neighborhood" TO "disaster-resilience";
GRANT SELECT ON TABLE public."neighborhood" TO "disaster-resilience-readonly";
