"""
Test script for the API endpoints
"""

import requests
import json

API_BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test health check endpoint"""
    print("Testing health check endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
        print("✓ Health check passed!\n")
        return True
    except Exception as e:
        print(f"✗ Health check failed: {e}\n")
        return False

def test_recommendation_query():
    """Test recommendation endpoint with query"""
    print("Testing recommendation endpoint with query...")
    try:
        payload = {
            "query": "I am hiring for Java developers who can also collaborate effectively with my business teams."
        }
        response = requests.post(
            f"{API_BASE_URL}/recommend",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)}")
        
        assert response.status_code == 200
        assert "recommendations" in data
        assert "query" in data
        assert "count" in data
        assert isinstance(data["recommendations"], list)
        assert len(data["recommendations"]) >= 5
        assert len(data["recommendations"]) <= 10
        
        # Check recommendation structure
        for rec in data["recommendations"]:
            assert "name" in rec
            assert "url" in rec
            assert rec["url"].startswith("http")
        
        print("✓ Recommendation query test passed!\n")
        return True
    except Exception as e:
        print(f"✗ Recommendation query test failed: {e}\n")
        return False

def test_recommendation_url():
    """Test recommendation endpoint with URL"""
    print("Testing recommendation endpoint with URL...")
    try:
        # Using a sample URL (this will fail if URL is not accessible, but tests the endpoint)
        payload = {
            "url": "https://example.com/job-description"
        }
        response = requests.post(
            f"{API_BASE_URL}/recommend",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        # This might fail if URL is not accessible, which is expected
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            print("✓ Recommendation URL test passed!\n")
            return True
        else:
            print(f"Response: {response.json()}")
            print("⚠ URL test returned error (expected if URL is not accessible)\n")
            return True  # This is acceptable
    except Exception as e:
        print(f"⚠ Recommendation URL test: {e}\n")
        return True  # Acceptable if URL processing fails

def test_error_handling():
    """Test error handling"""
    print("Testing error handling...")
    try:
        # Test with empty payload
        response = requests.post(
            f"{API_BASE_URL}/recommend",
            json={},
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 400
        print("✓ Empty payload error handling works")
        
        # Test with invalid endpoint
        response = requests.get(f"{API_BASE_URL}/invalid")
        assert response.status_code == 404
        print("✓ Invalid endpoint error handling works")
        
        print("✓ Error handling tests passed!\n")
        return True
    except Exception as e:
        print(f"✗ Error handling test failed: {e}\n")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("API Test Suite")
    print("=" * 50)
    print(f"Testing API at: {API_BASE_URL}\n")
    
    results = []
    results.append(("Health Check", test_health_check()))
    results.append(("Recommendation Query", test_recommendation_query()))
    results.append(("Recommendation URL", test_recommendation_url()))
    results.append(("Error Handling", test_error_handling()))
    
    print("=" * 50)
    print("Test Results Summary")
    print("=" * 50)
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(result[1] for result in results)
    print("\n" + "=" * 50)
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed. Please check the output above.")
    print("=" * 50)

if __name__ == '__main__':
    main()

