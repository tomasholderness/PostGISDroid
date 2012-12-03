CREATE TABLE droidtrack
(
  fid integer NOT NULL DEFAULT nextval('serial'::regclass),
  id integer NOT NULL,
  provider character varying(8) NOT NULL,
  accuracy real,
  altitude real,
  speed real,
  the_geom geometry,
  CONSTRAINT droidtrack_pkey PRIMARY KEY (fid)
);
