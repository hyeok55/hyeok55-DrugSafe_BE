# DrugSafe_Backend

Responsibility: Responsible for data processing, business logic processing, and integration with external services of DrugSafe.
Technology: Google Cloud Engine, Django, REST API

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

