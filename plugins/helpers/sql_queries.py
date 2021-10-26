class SqlQueries:
    playtype_table_create = ("""CREATE TABLE IF NOT EXISTS playtype(
                                                play_type_id smallint NOT NULL,
                                                play_type varchar(256) NOT NULL, 
                                                abbreviation varchar(10),
                            CONSTRAINT playtypes_pk PRIMARY KEY  (play_type_id); """)
