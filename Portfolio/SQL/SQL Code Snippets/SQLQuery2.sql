USE dbmovie
GO

ALTER TABLE tblmovie
ADD  m_Teaser VARCHAR(100)NOT NULL DEFAULT 'Prevert!', m_release INT NOT NULL DEFAULT 1*10^5
GO

SELECT *
FROM tblmovie

ALTER TABLE tblmovie
DROP COLUMN   m_release

DROP TABLE tblmovie
