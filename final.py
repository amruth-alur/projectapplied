def predict_crop_yield(year, highest_temp, lowest_temp, rainfall, humidity):
    beta0 = 1876698.8090531923
    beta1 = -931.6234744897814
    beta2 = 22.75540104746109
    beta3 = 93.30180468180479
    beta4 = -2.3335421086182023
    beta5 = -119.6017316017316
    
    crop_yield = (
        beta0 + beta1 * year + beta2 * highest_temp + beta3 * lowest_temp
        + beta4 * rainfall + beta5 * humidity
    )
    
    return crop_yield

# Example usage
year = 2021
highest_temp = 26
lowest_temp = 12
rainfall = 400
humidity = 60

predicted_yield = predict_crop_yield(year, highest_temp, lowest_temp, rainfall, humidity)
print("Predicted Crop Yield:", predicted_yield)
