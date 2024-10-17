# load modules
library(ggplot2)
library(readr)
library(tibble)
library(dplyr)
library(tidyr)

# load the data
kt <- read_csv("data/koopAndTobias/koop_tobias.csv")

# data preview
kt

# key features of the data

## observations
row_n <- n_distinct(kt)

## variables
col_n <- length(kt)

## unique cases
cases <- n_distinct(kt$PERSONID)

## wrap info regarding data's key features
key_features <- tribble(
  ~Observations, ~Variables, ~Cases,
  row_n, col_n, cases
)

# measurement occasions by individual
obs <- kt %>% group_by(PERSONID) %>% count()
ggplot(data = obs, mapping = aes(x = n)) +
  geom_bar()

# distribution of individuals by higher education level attained
max_ed <- kt %>% group_by(PERSONID) %>% summarise(max = max(EDUC))
ggplot(data = max_ed, mapping = aes(x = max)) + 
  geom_bar()

# distribution of log(hourly wage)
seq <- seq(0, 1, 0.05)
qf <- tibble(
  f = seq,
  qf = quantile(kt$LOGWAGE, probs = seq, names = FALSE)
)
ggplot(data = qf, mapping = aes(x = f, y = qf)) +
  geom_point()

ggplot(data = kt, mapping = aes(x = LOGWAGE)) +
  geom_histogram()

ggplot(data = kt, mapping = aes(y = LOGWAGE)) +
  geom_boxplot(orientation = "x")

# correlation between education and log(hourly wage)
ggplot(data = kt, mapping = aes(x = EDUC, y = LOGWAGE)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = lm)

ggplot(data = kt, mapping = aes(x = factor(EDUC), y = LOGWAGE)) +
  geom_boxplot()

ggplot(data = kt, mapping = aes(x = factor(EDUC), y = LOGWAGE)) +
  geom_violin(scale = "area")


# correlation between parents' education and log(hourly wage)
kt_pivot <- kt |> select(PERSONID, LOGWAGE, MOTHERED, FATHERED) %>% 
  pivot_longer(cols = ends_with("ED"))
ggplot(data = kt, mapping = aes(x = FATHERED, y = LOGWAGE)) +
  geom_point() + 
  geom