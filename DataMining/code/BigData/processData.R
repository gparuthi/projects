library("rjson")
library(plyr)

# here would be the code for all my R related processing

#read all lines into text
text <- readLines("delhi.1")

#get a json object for text... too slow
delhi->json = fromJSON(paste ('[',paste(text,collapse=',', sep=',') ,']'))

t_list = ldply(t$text,.fun=iconv)

GenWordCloud(laply(json, t_list)
#delhi.data = cbind(json, laply(json, function(t) t$text))
# no of words
length(ap.d[,1])
# get coordinates for people from new york
