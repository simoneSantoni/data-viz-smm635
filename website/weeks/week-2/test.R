library(ggplot2)

data <- economics

head(data)

ggplot(economics, aes(data$date, data$unemploy)) +
  geom_point() +
  geom_line(color = "red") +
  geom_area(color = "gray")
