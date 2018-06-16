-- table: public.neighborhood_loss_flat

-- drop table public.neighborhood_loss_flat;

create table public.neighborhood_loss_flat
(
	id integer not null,
	name  character varying(255),
	acres  character varying(255),
	buildingcount  character varying(255),
	buildingsquarefeet  character varying(255),
	buildingcost  character varying(255),
	buildingweight  character varying(255),
	contentcost  character varying(255),
	permanentresidents  character varying(255),
	dayoccupants  character varying(255),
	nightoccupants  character varying(255),
	buildingloss_wet  character varying(255),
	contentloss_wet  character varying(255),
	debris_wet  character varying(255),
	displacedpopulation_wet  character varying(255),
	buildings_nodamage_wet  character varying(255),
	buildings_slightdamage_wet  character varying(255),
	buildings_moderatedamage_wet  character varying(255),
	buildings_extensivedamage_wet  character varying(255),
	buildings_completedamage_wet  character varying(255),
	casualtiestotal_day_wet  character varying(255),
	casualtieslevel1_day_wet  character varying(255),
	casualtieslevel2_day_wet  character varying(255),
	casualtieslevel3_day_wet  character varying(255),
	fatalitiestotal_day_wet  character varying(255),
	casualtiestotal_night_wet  character varying(255),
	casualtieslevel1_night_wet  character varying(255),
	casualtieslevel2_night_wet  character varying(255),
	casualtieslevel3_night_wet  character varying(255),
	fatalitiestotal_night_wet  character varying(255),
	buildingloss_dry  character varying(255),
	contentloss_dry  character varying(255),
	debris_dry  character varying(255),
	displacedpopulation_dry  character varying(255),
	buildings_nodamage_dry  character varying(255),
	buildings_slightdamage_dry  character varying(255),
	buildings_moderatedamage_dry  character varying(255),
	buildings_extensivedamage_dry  character varying(255),
	buildings_completedamage_dry  character varying(255),
	casualtiestotal_day_dry  character varying(255),
	casualtieslevel1_day_dry  character varying(255),
	casualtieslevel2_day_dry  character varying(255),
	casualtieslevel3_day_dry  character varying(255),
	fatalitiestotal_day_dry  character varying(255),
	casualtiestotal_night_dry  character varying(255),
	casualtieslevel1_night_dry  character varying(255),
	casualtieslevel2_night_dry  character varying(255),
	casualtieslevel3_night_dry  character varying(255),
	fatalitiestotal_night_dry  character varying(255),
	injuriestotal_day_wet  character varying(255),
	injuriestotal_night_wet  character varying(255),
	injuriestotal_day_dry  character varying(255),
	injuriestotal_night_dry  character varying(255),
	total_population  character varying(255),
	displaced_percap_wet  character varying(255),
	displaced_percap_dry  character varying(255)
)
with (
  oids=false
);
alter table public.neighborhood_loss_flat
  owner to "disaster-resilience";
grant all on table public.neighborhood_loss_flat to "disaster-resilience";
grant select on table public.neighborhood_loss_flat to "disaster-resilience-readonly";
