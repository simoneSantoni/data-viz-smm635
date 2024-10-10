# load modules
library(ggplot2)

# sample viz
ggplot(data = mpg, mapping = aes(mpg, cyl)) + 
  geom_point()
