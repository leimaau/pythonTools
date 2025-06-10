set echo off
set trimspool on
set feedback off
set wrap off
set linesize 20000
set pagesize 20000
set newpage none
set heading off
set term off

spool E:\LocalRepository\github\\pythonTools\signPhrase\opencc\dictionary\jyutCharacters.txt
select trad||'	'||jyutping from v_nb_zingjam_signPhrase;

spool E:\LocalRepository\github\\pythonTools\signPhrase\opencc\dictionary\jyutCharacters_bw.txt
select trad||'	'||jyutping from v_nb_zingjam_bw_signPhrase;

spool E:\LocalRepository\github\\pythonTools\signPhrase\opencc\dictionary\jyutPhrases.txt
select trad||'	'||jyutping from (
	select distinct trad,replace(jyutping,' ','<s>')||'<s>' jyutping from v_Xiandaihanyu_Phrase_All where jyutping is not null and length(trad)>1
	union
	select trad,replace(jyutping,' ','<s>')||'<s>' jyutping from v_nb_zingjam_phrase
	where trad not in (select trad from v_Xiandaihanyu_Phrase_All where jyutping is not null)
	and trad not in (
		select trad from (
			select trad,count(jyutping) aa 
			from v_nb_zingjam_phrase 
			group by trad
		) where aa>1
	) and length(trad)>1
	union
	select trad,replace(jyutping,' ','<s>')||'<s>' jyutping from tab_nbdict_2020_phrase 
	where trad not in (select trad from v_Xiandaihanyu_Phrase_All where jyutping is not null)
	and trad not in (select trad from v_nb_zingjam_phrase)
	and trad not in (
		select trad from (
			select trad,count(jyutping) aa 
			from tab_nbdict_2020_phrase 
			group by trad
		) where aa>1
	) and length(trad)>1
) order by jyutping,trad;

spool E:\LocalRepository\github\\pythonTools\signPhrase\opencc\dictionary\jyutPhrases_bw.txt
select trad||'	'||jyutping from (
	select distinct trad,replace(jyutping,' ','<s>')||'<s>' jyutping from v_Xiandaihanyu_Phrase_Bw_All where jyutping is not null and length(trad)>1
	union
	select trad,replace(jyutping,' ','<s>')||'<s>' jyutping from tab_nbdict_2020_bw_phrase 
	where trad not in (select trad from v_Xiandaihanyu_Phrase_Bw_All where jyutping is not null)
	and trad not in (
		select trad from (
			select trad,count(jyutping) aa 
			from tab_nbdict_2020_bw_phrase 
			group by trad
		) where aa>1
	) and length(trad)>1
) order by jyutping,trad;

spool off