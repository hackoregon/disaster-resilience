-- Table: public.loss_neighborhood_census

-- DROP TABLE public.loss_neighborhood_census;

CREATE TABLE public.loss_neighborhood_census
(
  id integer NOT NULL DEFAULT nextval('neighborhood_loss_id_seq'::regclass),
  neighborhood_id integer NOT NULL,
  scenario_cd character varying(10),
  buildingloss character varying(255),
  contentloss character varying(255),
  debris character varying(255),
  displacedpopulation character varying(255),
  buildings_nodamage character varying(255),
  buildings_slightdamage character varying(255),
  buildings_moderatedamage character varying(255),
  buildings_extensivedamage character varying(255),
  buildings_completedamage character varying(255),
  casualtiestotal_day character varying(255),
  casualtieslevel1_day character varying(255),
  casualtieslevel2_day character varying(255),
  casualtieslevel3_day character varying(255),
  fatalitiestotal_day character varying(255),
  casualtiestotal_night character varying(255),
  casualtieslevel1_night character varying(255),
  casualtieslevel2_night character varying(255),
  casualtieslevel3_night character varying(255),
  fatalitiestotal_night character varying(255),
  injuriestotal_day character varying(255),
  injuriestotal_night character varying(255),
  displaced_percap character varying(255),
  CONSTRAINT neighborhood_loss_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.loss_neighborhood_census
  OWNER TO "disaster-resilience";
GRANT ALL ON TABLE public.loss_neighborhood_census TO "disaster-resilience";
GRANT SELECT ON TABLE public.loss_neighborhood_census TO "disaster-resilience-readonly";
