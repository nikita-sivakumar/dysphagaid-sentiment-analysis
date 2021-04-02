function dysphagia_reviews_analysis
%% Read Data from CSV file
table = readtable('dysphagia_combined_reviews.csv');
table.Properties.VariableNames = {'ReviewNum' 'Title' 'Review' 'Star' 'Product' 'Polarity' 'Subjectivity'};

%% Create Polarity BoxPlot
boxplot(table.Polarity, table.Product);
title('Polarity of Dysphagia Products')
xlabel('Product')
xtickangle(45)
ylabel('Polarity')

%% Create Subjectivity BoxPlot
boxplot(table.Subjectivity, table.Product);
title('Subjectivity of Dysphagia Products')
xlabel('Product')
xtickangle(45)
ylabel('Subjectivity')
end
