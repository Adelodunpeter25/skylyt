#!/usr/bin/env python3
"""
Database seeding script for Nigerian States and Cities
Creates the destination data needed for the destinations API
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import engine, SessionLocal
from app.models.state import State
from app.models.city import City
from sqlalchemy import text

def seed_nigerian_states_and_cities():
    """Seed the database with Nigerian states and cities"""
    
    db = SessionLocal()
    try:
        # Nigerian states data
        states_data = [
            {
                "name": "Lagos",
                "country": "Nigeria",
                "state_code": "LA",
                "slug": "lagos",
                "description": "Nigeria's economic hub and most populous state, home to Victoria Island, Lekki, and Ikoyi.",
                "popularity_score": 100.0,
                "is_featured": 1
            },
            {
                "name": "Abuja",
                "country": "Nigeria", 
                "state_code": "AB",
                "slug": "abuja",
                "description": "Nigeria's capital city, known for its modern architecture and political significance.",
                "popularity_score": 95.0,
                "is_featured": 1
            },
            {
                "name": "Rivers",
                "country": "Nigeria",
                "state_code": "RI",
                "slug": "rivers",
                "description": "Known for Port Harcourt, the oil and gas hub of Nigeria.",
                "popularity_score": 85.0,
                "is_featured": 1
            },
            {
                "name": "Kano",
                "country": "Nigeria",
                "state_code": "KN",
                "slug": "kano",
                "description": "Commercial center of Northern Nigeria with rich historical heritage.",
                "popularity_score": 80.0,
                "is_featured": 0
            },
            {
                "name": "Oyo",
                "country": "Nigeria",
                "state_code": "OY",
                "slug": "oyo",
                "description": "Home to Ibadan, the largest city in West Africa by land area.",
                "popularity_score": 75.0,
                "is_featured": 0
            },
            {
                "name": "Enugu",
                "country": "Nigeria",
                "state_code": "EN",
                "slug": "enugu",
                "description": "Known as the coal city and capital of Eastern Nigeria.",
                "popularity_score": 70.0,
                "is_featured": 0
            },
            {
                "name": "Delta",
                "country": "Nigeria",
                "state_code": "DE",
                "slug": "delta",
                "description": "Oil-rich state with Warri as its major city.",
                "popularity_score": 72.0,
                "is_featured": 0
            },
            {
                "name": "Ogun",
                "country": "Nigeria",
                "state_code": "OG",
                "slug": "ogun",
                "description": "Industrial state hosting many factories and industries.",
                "popularity_score": 68.0,
                "is_featured": 0
            }
        ]
        
        # Cities data mapped to states
        cities_data = {
            "lagos": [
                {"name": "Victoria Island", "slug": "victoria-island", "description": "Upscale neighborhood and business district", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Ikoyi", "slug": "ikoyi", "description": "Affluent residential and commercial area", "popularity_ranking": 2, "is_featured": 1},
                {"name": "Lekki", "slug": "lekki", "description": "Fast-growing peninsula with beaches and resorts", "popularity_ranking": 3, "is_featured": 1},
                {"name": "Lagos Island", "slug": "lagos-island", "description": "Historic business district with markets", "popularity_ranking": 4, "is_featured": 0},
                {"name": "Surulere", "slug": "surulere", "description": "Residential and commercial area", "popularity_ranking": 5, "is_featured": 0},
                {"name": "Ikeja", "slug": "ikeja", "description": "Capital of Lagos State with government offices", "popularity_ranking": 6, "is_featured": 0},
                {"name": "Yaba", "slug": "yaba", "description": "Education hub with many institutions", "popularity_ranking": 7, "is_featured": 0},
                {"name": "Maryland", "slug": "maryland", "description": "Residential and commercial district", "popularity_ranking": 8, "is_featured": 0},
            ],
            "abuja": [
                {"name": "Central Business District", "slug": "central-business-district", "description": "Prime business area with government buildings", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Maitama", "slug": "maitama", "description": "Exclusive residential district", "popularity_ranking": 2, "is_featured": 1},
                {"name": "Asokoro", "slug": "asokoro", "description": "High-end residential area", "popularity_ranking": 3, "is_featured": 1},
                {"name": "Wuse", "slug": "wuse", "description": "Commercial district with markets", "popularity_ranking": 4, "is_featured": 0},
                {"name": "Garki", "slug": "garki", "description": "Mixed residential and commercial area", "popularity_ranking": 5, "is_featured": 0},
                {"name": "Apapa", "slug": "apapa", "description": "Industrial area with port facilities", "popularity_ranking": 6, "is_featured": 0},
            ],
            "rivers": [
                {"name": "Port Harcourt", "slug": "port-harcourt", "description": "Oil and gas hub of Nigeria", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Obio-Akpor", "slug": "obio-akpor", "description": "Metropolitan area", "popularity_ranking": 2, "is_featured": 0},
                {"name": "Eleme", "slug": "eleme", "description": "Industrial area with refineries", "popularity_ranking": 3, "is_featured": 0},
            ],
            "kano": [
                {"name": "Kano City", "slug": "kano-city", "description": "Historic commercial center", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Nassarawa", "slug": "nassarawa", "description": "Residential area", "popularity_ranking": 2, "is_featured": 0},
                {"name": "Fagge", "slug": "fagge", "description": "Commercial district", "popularity_ranking": 3, "is_featured": 0},
            ],
            "oyo": [
                {"name": "Ibadan", "slug": "ibadan", "description": "Largest city in West Africa by land area", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Oyo", "slug": "oyo-city", "description": "Historic town with ancient walls", "popularity_ranking": 2, "is_featured": 0},
                {"name": "Ogbomosho", "slug": "ogbomosho", "description": "Major commercial city", "popularity_ranking": 3, "is_featured": 0},
            ],
            "enugu": [
                {"name": "Enugu City", "slug": "enugu-city", "description": "Capital city with coal mining history", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Nsukka", "slug": "nsukka", "description": "University town", "popularity_ranking": 2, "is_featured": 0},
                {"name": "Awgu", "slug": "awgu", "description": "Agricultural center", "popularity_ranking": 3, "is_featured": 0},
            ],
            "delta": [
                {"name": "Warri", "slug": "warri", "description": "Oil city and port", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Asaba", "slug": "asaba", "description": "State capital on the Niger River", "popularity_ranking": 2, "is_featured": 0},
                {"name": "Ughelli", "slug": "ughelli", "description": "Oil and gas town", "popularity_ranking": 3, "is_featured": 0},
            ],
            "ogun": [
                {"name": "Abeokuta", "slug": "abeokuta", "description": "State capital and historic city", "popularity_ranking": 1, "is_featured": 1},
                {"name": "Sagamu", "slug": "sagamu", "description": "Industrial town", "popularity_ranking": 2, "is_featured": 0},
                {"name": "Ijebu Ode", "slug": "ijebu-ode", "description": "Historic kingdom town", "popularity_ranking": 3, "is_featured": 0},
            ]
        }
        
        # Clear existing data
        print("Clearing existing states and cities...")
        db.query(City).delete()
        db.query(State).delete()
        db.commit()
        
        # Create states
        print("Creating states...")
        created_states = {}
        for state_data in states_data:
            existing_state = db.query(State).filter(State.slug == state_data["slug"]).first()
            if not existing_state:
                state = State(**state_data)
                db.add(state)
                db.commit()
                db.refresh(state)
                created_states[state.slug] = state.id
                print(f"  ✅ Created state: {state.name}")
            else:
                created_states[existing_state.slug] = existing_state.id
                print(f"  ℹ️ State already exists: {existing_state.name}")
        
        # Create cities
        print("Creating cities...")
        for state_slug, cities in cities_data.items():
            state_id = created_states.get(state_slug)
            if not state_id:
                print(f"  ⚠️ Warning: State {state_slug} not found, skipping cities")
                continue
            
            for city_data in cities:
                city_data["state_id"] = state_id
                existing_city = db.query(City).filter(
                    City.slug == city_data["slug"],
                    City.state_id == state_id
                ).first()
                
                if not existing_city:
                    city = City(**city_data)
                    db.add(city)
                    db.commit()
                    print(f"  ✅ Created city: {city.name} in {state_slug}")
                else:
                    print(f"  ℹ️ City already exists: {existing_city.name}")
        
        db.commit()
        print(f"\n✅ Successfully seeded {len(states_data)} states and {sum(len(cities) for cities in cities_data.values())} cities!")
        
        # Verify data
        print("\n📊 Verification:")
        state_count = db.query(State).count()
        city_count = db.query(City).count()
        print(f"  Total states: {state_count}")
        print(f"  Total cities: {city_count}")
        
        # Test the specific endpoint that was failing
        lagos_state = db.query(State).filter(State.slug == "lagos").first()
        if lagos_state:
            lagos_cities = db.query(City).filter(City.state_id == lagos_state.id).all()
            print(f"  Lagos state cities: {len(lagos_cities)}")
            print(f"  Lagos is featured: {lagos_state.is_featured}")
        else:
            print("  ⚠️ Lagos state not found!")
        
    except Exception as e:
        print(f"❌ Error seeding destinations: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("🌍 Starting Nigerian States and Cities Seeding...")
    seed_nigerian_states_and_cities()
    print("✅ Seeding complete!")