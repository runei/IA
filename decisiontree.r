tabela <- data.frame("A"=logical(1),"B"=logical(1),"C"=logical(1),"Class"=character(3), 
                     stringsAsFactors = FALSE);
for (i in 1:5){ tabela <- rbind(tabela, list(TRUE, TRUE, TRUE, "+")); }
for (i in 1:20){ tabela <- rbind(tabela, list(FALSE, TRUE, TRUE, "-")); }
for (i in 1:20){ tabela <- rbind(tabela, list(TRUE, FALSE, TRUE, "+")); }
for (i in 1:5){ tabela <- rbind(tabela, list(FALSE, FALSE, TRUE, "-")); }
for (i in 1:25){ tabela <- rbind(tabela, list(FALSE, TRUE, FALSE, "+")); }
for (i in 1:25){ tabela <- rbind(tabela, list(FALSE, FALSE, FALSE, "-")); }
tabela <- tabela[c(0:-3),]

library(rpart.plot)
library(DMwR)
set.seed(1234) # for reproduction
sample.tr <-sample(1:nrow(tabela),as.integer(0.7*nrow(tabela)))
tr <- tabela[sample.tr, ] #Split into two sets
ts <- tabela[-sample.tr,] 
model_tree <- rpartXse(n_offenses ~ .,tr)
preds_tree <- predict(model_tree,ts)
