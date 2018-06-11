-- Table: public.nets

DROP TABLE public.nets;

CREATE TABLE public.nets
(
  description_txt character varying NOT NULL,
  location_txt character varying,
  location_dms_val character varying,
  location_dd_val character varying,
  CONSTRAINT description_txt PRIMARY KEY (description_txt)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.nets
  OWNER TO "disaster-resilience";
  
GRANT ALL ON TABLE public."nets" TO "disaster-resilience";
GRANT SELECT ON TABLE public."nets" TO "disaster-resilience-readonly";

