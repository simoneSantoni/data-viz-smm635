# %%
library(tibble)
library(ggmap)

# %% toy data
# %% geospatial visualization 
ny_map <- get_googlemap(
  #center = c(lon = -74.0060, lat = 40.7128),
  center = "New York",
  zoom = 11,
  size = c(1200, 1200),
  maptype = "hybrid",
)
ggmap(ny_map) +
  geom_label(data = unis, color = "purple", label = unis$name, size = 5) +
  theme_nothing()

# %%
get_googlemap(
  center = c(lon = -74.0060, lat = 40.7128),
  markers = unis[, c("lon", "lat")],
  zoom = 11,
  size = c(1200, 1200),
  maptype = "hybrid",
) |> ggmap()
