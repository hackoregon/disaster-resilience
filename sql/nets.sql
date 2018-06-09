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

COPY nets(description_txt, location_txt, location_dms_val, location_dd_val)
FROM 'C:\develop\hackoregon\disaster\NET_deployment_sites.csv' DELIMITER ',' CSV HEADER;
