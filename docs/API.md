# API Documentation

Documentation for CEANAPSE Donation Platform API endpoints.

## Base URL

- **Development**: `http://127.0.0.1:8000/api/`
- **Production**: `https://ceanapse.org/api/`

## Authentication

Most endpoints are public. Admin endpoints require Django session authentication.

---

## Endpoints

### 1. Initiate Donation

**Endpoint:** `POST /api/donations/initiate/`

**Description:** Creates a donation record and returns Paystack payment URL.

**Request Body:**
```json
{
    "donor_name": "John Doe",
    "donor_email": "john@example.com",
    "donor_phone": "+254700000000",
    "amount": 1000
}
```

**Response (Success - 200):**
```json
{
    "status": "success",
    "message": "Payment initialized",
    "data": {
        "authorization_url": "https://checkout.paystack.com/xxxxx",
        "access_code": "xxxxx",
        "reference": "CEAN-xxxxx"
    }
}
```

**Response (Error - 400):**
```json
{
    "status": "error",
    "message": "Invalid data",
    "errors": {
        "donor_email": ["Enter a valid email address."],
        "amount": ["Amount must be greater than 0."]
    }
}
```

---

### 2. Verify Payment

**Endpoint:** `GET /api/donations/verify/<reference>/`

**Description:** Verifies payment status with Paystack and updates database.

**URL Parameters:**
- `reference` (string): Payment reference from Paystack

**Response (Success - 200):**
```json
{
    "status": "success",
    "message": "Payment verified successfully",
    "data": {
        "reference": "CEAN-xxxxx",
        "amount": 1000,
        "donor_name": "John Doe",
        "donor_email": "john@example.com",
        "status": "success",
        "transaction_date": "2024-11-03T10:30:00Z"
    }
}
```

**Response (Failed Payment - 200):**
```json
{
    "status": "failed",
    "message": "Payment was not successful",
    "data": {
        "reference": "CEAN-xxxxx",
        "status": "failed"
    }
}
```

---

### 3. Paystack Webhook

**Endpoint:** `POST /api/donations/webhook/`

**Description:** Receives payment notifications from Paystack.

**Headers:**
```
x-paystack-signature: <signature_hash>
```

**Request Body (from Paystack):**
```json
{
    "event": "charge.success",
    "data": {
        "reference": "CEAN-xxxxx",
        "amount": 100000,
        "status": "success",
        "customer": {
            "email": "john@example.com"
        }
    }
}
```

**Response (200):**
```json
{
    "status": "success"
}
```

---

### 4. Get Donation Statistics (Admin)

**Endpoint:** `GET /api/admin/statistics/`

**Description:** Returns donation statistics for admin dashboard.

**Authentication:** Required (Django Admin session)

**Response (200):**
```json
{
    "total_donations": 50,
    "total_amount": 500000,
    "successful_donations": 45,
    "failed_donations": 5,
    "pending_donations": 0,
    "top_donors": [
        {
            "donor_name": "John Doe",
            "donor_email": "john@example.com",
            "total_donated": 50000,
            "donation_count": 5
        }
    ],
    "recent_donations": [
        {
            "reference": "CEAN-xxxxx",
            "donor_name": "Jane Smith",
            "amount": 10000,
            "status": "success",
            "date": "2024-11-03T10:30:00Z"
        }
    ]
}
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid data |
| 401 | Unauthorized - Authentication required |
| 404 | Not Found - Resource doesn't exist |
| 500 | Server Error - Something went wrong |

---

## Data Models

### Donation Model
```python
{
    "id": 1,
    "donor_name": "John Doe",
    "donor_email": "john@example.com",
    "donor_phone": "+254700000000",
    "amount": 1000.00,
    "reference": "CEAN-xxxxx",
    "status": "success",  # pending, success, failed
    "transaction_date": "2024-11-03T10:30:00Z",
    "paystack_response": {...}  # Full Paystack response JSON
}
```

---

## Paystack Integration

### Configuration
```python
# In settings.py or .env
PAYSTACK_SECRET_KEY = "sk_test_xxxxx"  # Test key
PAYSTACK_PUBLIC_KEY = "pk_test_xxxxx"  # Test key
PAYSTACK_WEBHOOK_SECRET = "webhook_secret"
```

### Test Cards (Paystack Test Mode)

| Card Number | CVV | PIN | OTP | Result |
|-------------|-----|-----|-----|--------|
| 4084084084084081 | 408 | 0000 | 123456 | Success |
| 5060666666666666666 | 123 | 1234 | 123456 | Insufficient funds |

---

## Frontend Integration Example

### JavaScript (Donation Form)
```javascript
// Submit donation form
async function initiateDonation(formData) {
    try {
        const response = await fetch('/api/donations/initiate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            // Redirect to Paystack
            window.location.href = data.data.authorization_url;
        } else {
            // Handle error
            console.error(data.message);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
```

---

## Rate Limiting

*To be implemented in production*

- **Public endpoints**: 100 requests/hour per IP
- **Admin endpoints**: 1000 requests/hour per user

---

## Webhooks Setup

### Configure in Paystack Dashboard

1. Go to Settings → Webhooks
2. Add URL: `https://your domain.org/api/donations/webhook/`
3. Copy webhook secret to `.env`

### Testing Webhooks Locally

Use [ngrok](https://ngrok.com/) to expose local server:
```bash
# Start Django server
python manage.py runserver

# In another terminal
ngrok http 8000

# Use ngrok URL in Paystack webhook settings
# Example: https://xxxx.ngrok.io/api/donations/webhook/
```

---

## Questions?

Contact Dev 2 (Alphonce) for payment-related questions or Dev 3 (Ismael) for infrastructure questions.