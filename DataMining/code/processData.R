library("rjson")
library(plyr)

# here would be the code for all my R related processing

#



read all lines into text
text <- readLines("gardenhose.2012-11-01.gz.data")

#get a json object for text... too slow
json = fromJSON(paste ('[',paste(text,collapse=',', sep=',') ,']'))

af = NULL
infile = "gardenhose.2012-11-01.gz.data"
con  <- file(inputFile, open = "r")
dataList <- list()
con  <- file(infile, open = "r")
while (length(oneLine <- readLines(con, n = 1, warn = FALSE)) > 0) {
af <- rbind(af, fromJSON(oneLine))
}



# get coordinates for people from new york
