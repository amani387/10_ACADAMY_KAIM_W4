

# Sales distribution
plt.figure(figsize=(10, 6))
sns.histplot(cleaned_train_merged['Sales'], bins=50, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
 


# Sales during promotions
plt.figure(figsize=(10, 6))
sns.boxplot(x='Promo', y='Sales', data=train_merged)
plt.title("Sales vs. Promotions")
plt.xlabel("Promo")
plt.ylabel("Sales")
plt.show()




# Convert Date column to datetime
train_merged['Date'] = pd.to_datetime(train_merged['Date'])

# Sales trend over time
plt.figure(figsize=(14, 7))
train_merged.groupby('Date')['Sales'].sum().plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()




# Sales during holidays
plt.figure(figsize=(10, 6))
sns.boxplot(x='StateHoliday', y='Sales', data=train_merged)
plt.title("Sales vs. State Holidays")
plt.xlabel("State Holiday")
plt.ylabel("Sales")
plt.show()
