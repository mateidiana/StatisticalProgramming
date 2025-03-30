# INSTALL AND LOAD PACKAGES ################################

library(datasets)  # Load base packages manually

# Installs pacman ("package manager") if needed
if (!require("pacman")) install.packages("pacman")

# Use pacman to load add-on packages as desired
pacman::p_load(pacman, caret, lars, tidyverse)

# LOAD DATA ################################################

?USJudgeRatings
head(USJudgeRatings)
data <- USJudgeRatings

# Define variable groups
x <- as.matrix(data[, -12])
y <- data[, 12]

# REGRESSION WITH SIMULTANEOUS ENTRY #######################

# Using variable groups
reg1 <- lm(y ~ x)

# Results
summary(reg1)  # Inferential tests

# MORE SUMMARIES ###########################################
resid(reg1)            # Residuals case-by-case
hist(residuals(reg1))  # Histogram of residuals


# CLEAN UP #################################################

# Clear environment
rm(list = ls()) 

# Clear packages
p_unload(all)  # Remove all add-ons
detach("package:datasets", unload = TRUE)  # For base

# Clear plots
dev.off()  # But only if there IS a plot

# Clear console
cat("\014")
