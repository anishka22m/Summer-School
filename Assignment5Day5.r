# Load required libraries
library(dplyr)
library(tidyr)
library(Matrix)
library(cluster)
library(gplots)
library(stats)

# Set random seed for reproducibility
set.seed(123)

# Q1: Create a file with random strings
random_strings <- replicate(1000, paste(sample(letters, 10, replace = TRUE), collapse = ""))
writeLines(random_strings, "random_strings.txt")

# Q2: Create a random dataset and perform operations
random_data <- matrix(sample(1:200, 100 * 30, replace = TRUE), ncol = 30)
random_data[10:60, ] <- NA
missing_rows <- sum(rowSums(is.na(random_data)) > 0)
cat("Number of rows with missing values:", missing_rows, "\n")

random_data[is.na(random_data)] <- colMeans(random_data, na.rm = TRUE)[col(random_data)]
cor_matrix <- cor(random_data)
cor_plot <- heatmap(cor_matrix, symm = TRUE)

high_cor_cols <- which(apply(cor_matrix, 2, function(x) any(x <= 0.7)))
cat("Columns with correlation <= 0.7:", high_cor_cols, "\n")

normalized_data <- scale(random_data, center = FALSE, scale = 10/(max(random_data) - min(random_data)))

binarized_data <- ifelse(random_data <= 0.5, 1, 0)

# Q3: Clustering algorithms
random_data_2 <- matrix(c(
  runif(500, -10, 10),
  runif(500, -10, 10),
  runif(500, -10, 10),
  runif(500, -10, 10),
  runif(500, 10, 20),
  runif(500, 10, 20),
  runif(500, 10, 20),
  runif(500, 10, 20),
  runif(500, -100, 100),
  runif(500, -100, 100)
), ncol = 10)

# K-Means clustering
kmeans_dist <- dist(random_data_2)
kmeans_fit <- kmeans(random_data_2, centers = 3)
plot(hclust(kmeans_dist), main = "K-Means Clustering")

# Hierarchical clustering
hierarchical_dist <- dist(random_data_2)
plot(hclust(hierarchical_dist), main = "Hierarchical Clustering")

# Q4: Visualizations
random_data_3 <- matrix(runif(600, -100, 100), ncol = 15)
colnames(random_data_3) <- paste("Column", 1:15)

# Scatter plot
plot(random_data_3[, 5], random_data_3[, 6], xlab = "Column 5", ylab = "Column 6", main = "Scatter Plot")

# Histograms
par(mfrow = c(3, 5))
for (i in 1:15) {
  hist(random_data_3[, i], main = colnames(random_data_3)[i], xlab = "")
}

# Box plots
boxplot(random_data_3, main = "Box Plots")

# Q5: Statistical tests
random_data_4 <- matrix(runif(500, 5, 10), ncol = 5)

# Perform t-Test on each column
t_test_results <- lapply(1:ncol(random_data_4), function(i) {
  t.test(random_data_4[, i])
})

# Perform Wilcoxon Signed Rank Test on each column
wilcox_test_results <- lapply(1:ncol(random_data_4), function(i) {
  wilcox.test(random_data_4[, i], mu = 7.5)
})

# Perform Two Sample t-Test and Wilcoxon Rank Sum Test on Column 3 and Column 4
t_test_3_4 <- t.test(random_data_4[, 3], random_data_4[, 4])
wilcox_test_3_4 <- wilcox.test(random_data_4[, 3], random_data_4[, 4])

# Print test results
print(t_test_results)
print(wilcox_test_results)
print(t_test_3_4)
print(wilcox_test_3_4)
