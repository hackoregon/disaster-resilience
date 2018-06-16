-- Table: public.neighborhood

-- DROP TABLE public.neighborhood;

CREATE TABLE public.neighborhood
(
  id integer NOT NULL,
  name character varying(255),
  census_response_rate character varying(255),
  quadrant character varying(255),
  acres character varying(255),
  buildingcount character varying(255),
  buildingsquarefeet character varying(255),
  buildingcost character varying(255),
  buildingweight character varying(255),
  contentcost character varying(255),
  permanentresidents character varying(255),
  dayoccupants character varying(255),
  nightoccupants character varying(255),
  total_population character varying(255),
  CONSTRAINT neighborhood_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.neighborhood
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public.neighborhood TO "disaster-resilience";
GRANT SELECT ON TABLE public.neighborhood TO "disaster-resilience-readonly";
