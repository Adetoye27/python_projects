#Write a program will display the account id from the arn below: arn:aws.iam:123456789012:user/Development/product_1234/*
# Display on the screen: the aws account id is: account id.

aws_arn = "arn:aws.iam:123456789012:user/Development/product_1234/*"

#using the split method and picking the index of the account number
account_id = aws_arn.split(":")[2]

print(f"The aws account id is: {account_id}")
