# Backend

Responsible for data processing, business logic processing, and integration with external services of DrugSafe.

# Technology
<img width="584" alt="image" src="https://github.com/hyeok55/hyeok55-DrugSafe_BE/assets/67605795/0054ebcd-0101-40d2-bce3-f0582789c2f8">
<img width="584" alt="image" src="https://github.com/hyeok55/hyeok55-DrugSafe_BE/assets/67605795/e64a3de7-8804-4325-8b1c-a22f3f915c25">
<img width="486" alt="image" src="https://github.com/hyeok55/hyeok55-DrugSafe_BE/assets/67605795/113a31d6-0989-4f24-9f0a-3ceb1f7d6ff1">



## What is DrugSafe?
<img width="317" alt="image" src="https://github.com/hyeok55/solution_challenge_2024/assets/67605795/481a7265-2721-4f0c-8cec-b8a4d4445c10">


The drug problem is serious worldwide. It is a project that helps to inform and prevent the seriousness and risk of drug addiction in order to solve these problems and create a healthier society. DrugSafe provides prediction of the risk of drug abuse and side effects of facial aging when drug abuse is performed, and lists drug mortality, interest, and drugs by type.


## API
### Main page
safeguardian/ 

### List Drugs by Category Page
safeguardian/drug/<int:ctgry_id> 

### Request a detailed drug page on the Category page
safeguardian/drug_type/<int:drug_id>

### Drug search page
safeguardian/search/

###Forward to unintended drug case page
safeguardian/unintention/<int:usage_id>

