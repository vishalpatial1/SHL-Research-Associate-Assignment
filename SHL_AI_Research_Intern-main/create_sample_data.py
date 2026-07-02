"""
Create sample assessment data for testing
This simulates the scraped data from SHL catalog
"""

import json
import os

# Sample SHL assessments based on the catalog structure
sample_assessments = [
    {
        "name": "OPQ32 (Occupational Personality Questionnaire)",
        "url": "https://www.shl.com/solutions/products/opq32/",
        "description": "Comprehensive personality assessment measuring behavioral preferences and work styles. Helps identify how individuals prefer to work, interact with others, and approach tasks.",
        "test_type": "Personality & Behavior",
        "skills": ["Personality", "Behavioral Preferences", "Work Styles", "Interpersonal Skills"]
    },
    {
        "name": "Verify G+",
        "url": "https://www.shl.com/solutions/products/verify-g-plus/",
        "description": "Cognitive ability test measuring numerical, verbal, and abstract reasoning. Assesses general mental ability and problem-solving skills.",
        "test_type": "Knowledge & Skills",
        "skills": ["Numerical Reasoning", "Verbal Reasoning", "Abstract Reasoning", "Problem Solving"]
    },
    {
        "name": "Verify Interactive",
        "url": "https://www.shl.com/solutions/products/verify-interactive/",
        "description": "Interactive cognitive ability assessment using game-based scenarios to measure problem-solving and decision-making abilities.",
        "test_type": "Knowledge & Skills",
        "skills": ["Problem Solving", "Decision Making", "Cognitive Ability", "Interactive Assessment"]
    },
    {
        "name": "Verify Numerical",
        "url": "https://www.shl.com/solutions/products/verify-numerical/",
        "description": "Focused assessment of numerical reasoning and mathematical problem-solving abilities. Ideal for roles requiring quantitative skills.",
        "test_type": "Knowledge & Skills",
        "skills": ["Numerical Reasoning", "Mathematical Ability", "Data Analysis", "Quantitative Skills"]
    },
    {
        "name": "Verify Verbal",
        "url": "https://www.shl.com/solutions/products/verify-verbal/",
        "description": "Assessment of verbal reasoning, comprehension, and communication skills. Evaluates ability to understand and analyze written information.",
        "test_type": "Knowledge & Skills",
        "skills": ["Verbal Reasoning", "Reading Comprehension", "Communication", "Language Skills"]
    },
    {
        "name": "Verify Inductive",
        "url": "https://www.shl.com/solutions/products/verify-inductive/",
        "description": "Measures inductive reasoning ability through pattern recognition and logical thinking tasks.",
        "test_type": "Knowledge & Skills",
        "skills": ["Inductive Reasoning", "Pattern Recognition", "Logical Thinking", "Analytical Skills"]
    },
    {
        "name": "Verify Deductive",
        "url": "https://www.shl.com/solutions/products/verify-deductive/",
        "description": "Assesses deductive reasoning skills through logical sequence and rule-based problem solving.",
        "test_type": "Knowledge & Skills",
        "skills": ["Deductive Reasoning", "Logical Reasoning", "Rule-Based Thinking", "Analytical Skills"]
    },
    {
        "name": "Verify Mechanical",
        "url": "https://www.shl.com/solutions/products/verify-mechanical/",
        "description": "Evaluates mechanical reasoning and understanding of physical principles. Suitable for technical and engineering roles.",
        "test_type": "Knowledge & Skills",
        "skills": ["Mechanical Reasoning", "Technical Understanding", "Engineering Principles", "Physical Concepts"]
    },
    {
        "name": "Verify Calculation",
        "url": "https://www.shl.com/solutions/products/verify-calculation/",
        "description": "Tests basic mathematical calculation skills and numerical accuracy. Essential for roles requiring precise numerical work.",
        "test_type": "Knowledge & Skills",
        "skills": ["Mathematical Calculation", "Numerical Accuracy", "Basic Math", "Computational Skills"]
    },
    {
        "name": "MOTIFY",
        "url": "https://www.shl.com/solutions/products/motify/",
        "description": "Motivation and values assessment that identifies what drives individuals and aligns with organizational culture.",
        "test_type": "Personality & Behavior",
        "skills": ["Motivation", "Values", "Cultural Fit", "Work Motivation"]
    },
    {
        "name": "Situational Judgment Test (SJT)",
        "url": "https://www.shl.com/solutions/products/situational-judgment-test/",
        "description": "Evaluates judgment and decision-making in work-related scenarios. Measures practical intelligence and job-relevant competencies.",
        "test_type": "Personality & Behavior",
        "skills": ["Judgment", "Decision Making", "Practical Intelligence", "Work Competencies"]
    },
    {
        "name": "Verify Coding",
        "url": "https://www.shl.com/solutions/products/verify-coding/",
        "description": "Programming skills assessment for software development roles. Tests coding ability in multiple programming languages.",
        "test_type": "Knowledge & Skills",
        "skills": ["Programming", "Coding", "Software Development", "Technical Skills"]
    },
    {
        "name": "Verify Java",
        "url": "https://www.shl.com/solutions/products/verify-java/",
        "description": "Java programming assessment specifically designed for Java developer roles. Evaluates Java-specific knowledge and coding skills.",
        "test_type": "Knowledge & Skills",
        "skills": ["Java Programming", "Object-Oriented Programming", "Java Development", "Technical Skills"]
    },
    {
        "name": "Verify Python",
        "url": "https://www.shl.com/solutions/products/verify-python/",
        "description": "Python programming assessment for Python developer positions. Tests Python syntax, libraries, and best practices.",
        "test_type": "Knowledge & Skills",
        "skills": ["Python Programming", "Python Libraries", "Scripting", "Technical Skills"]
    },
    {
        "name": "Verify JavaScript",
        "url": "https://www.shl.com/solutions/products/verify-javascript/",
        "description": "JavaScript and web development assessment. Evaluates front-end development skills and JavaScript proficiency.",
        "test_type": "Knowledge & Skills",
        "skills": ["JavaScript", "Web Development", "Front-End Development", "Technical Skills"]
    },
    {
        "name": "Verify SQL",
        "url": "https://www.shl.com/solutions/products/verify-sql/",
        "description": "SQL database skills assessment. Tests ability to write queries, understand database structures, and manipulate data.",
        "test_type": "Knowledge & Skills",
        "skills": ["SQL", "Database Management", "Data Querying", "Technical Skills"]
    },
    {
        "name": "Talent Q Elements",
        "url": "https://www.shl.com/solutions/products/talent-q-elements/",
        "description": "Comprehensive assessment suite measuring personality, ability, and motivation. Provides holistic view of candidate potential.",
        "test_type": "Personality & Behavior",
        "skills": ["Personality", "Ability", "Motivation", "Holistic Assessment"]
    },
    {
        "name": "MFS (Management and Feedback System)",
        "url": "https://www.shl.com/solutions/products/mfs/",
        "description": "Leadership and management assessment focusing on management competencies and feedback skills.",
        "test_type": "Personality & Behavior",
        "skills": ["Leadership", "Management", "Feedback Skills", "Management Competencies"]
    },
    {
        "name": "Verify Cognitive Ability",
        "url": "https://www.shl.com/solutions/products/verify-cognitive-ability/",
        "description": "General cognitive ability assessment combining multiple reasoning domains. Provides overall measure of intellectual capability.",
        "test_type": "Knowledge & Skills",
        "skills": ["Cognitive Ability", "General Intelligence", "Reasoning", "Problem Solving"]
    },
    {
        "name": "OPQ32r",
        "url": "https://www.shl.com/solutions/products/opq32r/",
        "description": "Revised version of OPQ32 with updated norms and improved psychometric properties. Measures personality and behavioral preferences.",
        "test_type": "Personality & Behavior",
        "skills": ["Personality", "Behavioral Preferences", "Work Styles", "Interpersonal Skills"]
    },
    {
        "name": "Verify Abstract",
        "url": "https://www.shl.com/solutions/products/verify-abstract/",
        "description": "Abstract reasoning assessment measuring ability to identify patterns and solve non-verbal problems.",
        "test_type": "Knowledge & Skills",
        "skills": ["Abstract Reasoning", "Pattern Recognition", "Non-Verbal Reasoning", "Logical Thinking"]
    },
    {
        "name": "Verify Spatial",
        "url": "https://www.shl.com/solutions/products/verify-spatial/",
        "description": "Spatial reasoning assessment evaluating ability to visualize and manipulate objects in three-dimensional space.",
        "test_type": "Knowledge & Skills",
        "skills": ["Spatial Reasoning", "Visualization", "3D Thinking", "Technical Skills"]
    },
    {
        "name": "Verify Error Checking",
        "url": "https://www.shl.com/solutions/products/verify-error-checking/",
        "description": "Attention to detail assessment measuring ability to identify errors and inconsistencies in data or text.",
        "test_type": "Knowledge & Skills",
        "skills": ["Attention to Detail", "Error Detection", "Quality Control", "Accuracy"]
    },
    {
        "name": "Verify Checking",
        "url": "https://www.shl.com/solutions/products/verify-checking/",
        "description": "Data checking and verification assessment. Tests ability to compare and verify information accurately.",
        "test_type": "Knowledge & Skills",
        "skills": ["Data Verification", "Information Checking", "Accuracy", "Attention to Detail"]
    },
    {
        "name": "Talent Q Dimensions",
        "url": "https://www.shl.com/solutions/products/talent-q-dimensions/",
        "description": "Personality assessment measuring key dimensions of workplace behavior and preferences.",
        "test_type": "Personality & Behavior",
        "skills": ["Personality", "Workplace Behavior", "Behavioral Preferences", "Work Styles"]
    },
    {
        "name": "Verify Technical",
        "url": "https://www.shl.com/solutions/products/verify-technical/",
        "description": "Technical skills assessment covering various technical domains and engineering principles.",
        "test_type": "Knowledge & Skills",
        "skills": ["Technical Skills", "Engineering", "Technical Knowledge", "Problem Solving"]
    },
    {
        "name": "Verify Critical Thinking",
        "url": "https://www.shl.com/solutions/products/verify-critical-thinking/",
        "description": "Critical thinking and analytical reasoning assessment. Evaluates ability to analyze information and make reasoned judgments.",
        "test_type": "Knowledge & Skills",
        "skills": ["Critical Thinking", "Analytical Reasoning", "Judgment", "Problem Solving"]
    },
    {
        "name": "Verify Business Judgment",
        "url": "https://www.shl.com/solutions/products/verify-business-judgment/",
        "description": "Business acumen and commercial judgment assessment. Tests understanding of business principles and decision-making.",
        "test_type": "Knowledge & Skills",
        "skills": ["Business Acumen", "Commercial Judgment", "Business Understanding", "Decision Making"]
    },
    {
        "name": "Verify Customer Service",
        "url": "https://www.shl.com/solutions/products/verify-customer-service/",
        "description": "Customer service skills and competencies assessment. Evaluates ability to handle customer interactions effectively.",
        "test_type": "Personality & Behavior",
        "skills": ["Customer Service", "Interpersonal Skills", "Communication", "Service Orientation"]
    },
    {
        "name": "Verify Sales",
        "url": "https://www.shl.com/solutions/products/verify-sales/",
        "description": "Sales skills and competencies assessment. Measures ability to identify opportunities, build relationships, and close deals.",
        "test_type": "Personality & Behavior",
        "skills": ["Sales Skills", "Relationship Building", "Persuasion", "Commercial Skills"]
    }
]

def create_data_directory():
    """Create data directory if it doesn't exist"""
    os.makedirs('data', exist_ok=True)

def save_assessments():
    """Save sample assessments to JSON file"""
    create_data_directory()
    filepath = 'data/assessments.json'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(sample_assessments, f, indent=2, ensure_ascii=False)
    
    print(f"Created {filepath} with {len(sample_assessments)} assessments")
    return filepath

if __name__ == '__main__':
    save_assessments()
    print(f"\nSample data created successfully!")
    print(f"Total assessments: {len(sample_assessments)}")
    print("\nNote: In production, you would run scraper.py to get real data from SHL catalog.")

