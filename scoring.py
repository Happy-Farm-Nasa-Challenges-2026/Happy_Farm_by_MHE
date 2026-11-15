import pandas as pd

# ============================================
# 1. Crop Information
# ============================================
CROPS = {
    "Wheat": {
        "type": "cereal",
        "season": "winter",
        "ideal_temp": (12, 20),
        "water_need_mm": 450,          # approximate seasonal need
        "n_fixation": False,
        "notes": "Common winter cereal in the Delta"
    },
    "Maize": {
        "type": "cereal",
        "season": "summer",
        "ideal_temp": (22, 32),
        "water_need_mm": 550,
        "n_fixation": False,
        "notes": "Heavy feeder, high water demand"
    },
    "Rice": {
        "type": "cereal",
        "season": "summer",
        "ideal_temp": (25, 35),
        "water_need_mm": 900,
        "n_fixation": False,
        "notes": "Very high water requirement"
    },
    "Berseem": {
        "type": "legume",
        "season": "winter",
        "ideal_temp": (12, 22),
        "water_need_mm": 350,
        "n_fixation": True,
        "notes": "Excellent nitrogen fixer and soil improver"
    },
    "Faba Bean": {
        "type": "legume",
        "season": "winter",
        "ideal_temp": (10, 20),
        "water_need_mm": 300,
        "n_fixation": True,
        "notes": "Good nitrogen fixer, common in rotations"
    }
}

# ============================================
# 2. Rotation Rules (Previous crop → Bonus)
# ============================================
def get_rotation_score(previous_crop, candidate):
    prev_type = CROPS[previous_crop]["type"]
    cand_type = CROPS[candidate]["type"]

    # Best practice: Cereal → Legume
    if prev_type == "cereal" and cand_type == "legume":
        return 90
    # Legume → Cereal is also good
    if prev_type == "legume" and cand_type == "cereal":
        return 85
    # Same type is less ideal
    if prev_type == cand_type:
        return 40
    # Default
    return 60

# ============================================
# 3. Climate Suitability Score
# ============================================
def climate_score(crop_name, avg_temp):
    ideal_min, ideal_max = CROPS[crop_name]["ideal_temp"]
    
    if ideal_min <= avg_temp <= ideal_max:
        return 95
    elif abs(avg_temp - (ideal_min + ideal_max)/2) < 5:
        return 75
    else:
        return 45

# ============================================
# 4. Water Balance Score
# ============================================
def water_score(crop_name, recent_rain_mm):
    need = CROPS[crop_name]["water_need_mm"]
    
    # Very simple logic for Delta (irrigation is common)
    if need < 400:
        return 90          # low water crops are better
    elif need < 600:
        return 70
    else:
        return 40          # rice is water hungry

# ============================================
# 5. Main Scoring Function
# ============================================
def recommend_rotations(previous_crop, climate_df, top_n=4):
    # Calculate average temperature and rainfall from recent years
    avg_temp = climate_df["T2M"].mean()
    total_rain = climate_df["PRECTOTCORR"].mean() * 30 * 6   # rough 6-month estimate
    
    results = []

    for crop in CROPS:
        if crop == previous_crop:
            continue  # skip recommending the same crop

        # Individual scores
        clim = climate_score(crop, avg_temp)
        water = water_score(crop, total_rain)
        rotation = get_rotation_score(previous_crop, crop)
        soil = 90 if CROPS[crop]["n_fixation"] else 50

        # Weighted total score
        total = (clim * 0.35) + (water * 0.25) + (rotation * 0.25) + (soil * 0.15)

        # Generate simple explanation
        reasons = []
        if CROPS[crop]["n_fixation"]:
            reasons.append("Fixes nitrogen and improves soil")
        if clim >= 80:
            reasons.append("Good temperature match")
        if water >= 80:
            reasons.append("Lower water requirement")
        if rotation >= 80:
            reasons.append("Excellent rotation after " + previous_crop)

        results.append({
            "crop": crop,
            "score": round(total, 1),
            "reasons": " | ".join(reasons) if reasons else "Moderate fit",
            "type": CROPS[crop]["type"],
            "season": CROPS[crop]["season"]
        })

    # Sort by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results[:top_n]

# ============================================
# Test the function
# ============================================
if __name__ == "__main__":
    df = load_nasa_power()
    
    print("=== Testing recommendations after Maize ===")
    recs = recommend_rotations("Maize", df)
    
    for r in recs:
        print(f"{r['crop']:12} | Score: {r['score']} | {r['reasons']}")