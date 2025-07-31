# 🛰️ Drone Deconfliction System (3D + Time)

This project implements a **strategic drone conflict detection system** in shared airspace. It validates whether a drone's waypoint-based mission is safe to execute by checking for **spatial and temporal conflicts** against other simulated drones.

✅ Designed for the FlytBase Robotics Assignment 2025  
✅ Built with modular, testable, and scalable architecture  
✅ Includes 3D visualization of drone paths and conflict zones

---

## ✈️ Use Case

In a shared airspace scenario, multiple drones may operate simultaneously. This system checks:

- Whether a new drone mission **conflicts spatially** (within a safety distance)
- Whether the conflict also **overlaps in time**
- And if so, it identifies the **conflicting segments, times, and points**

---

## 📁 Project Structure

```
drone_deconfliction/
├── main.py                  # Entry point to run the system
├── requirements.txt         # Dependencies (numpy, matplotlib)
├── .gitignore
├── data/
│   └── sample_missions.json # Example drone missions
├── models/
│   ├── waypoint.py          # Waypoint with x, y, z, t
│   └── mission.py           # DroneMission class
├── core/
│   ├── spatial.py           # Segment-to-segment distance calculation
│   ├── temporal.py          # Time overlap checker
│   └── conflict_checker.py  # Main conflict detection logic
├── utils/
│   ├── data_loader.py       # Load missions from JSON
│   └── visualizer.py        # 3D visualization using matplotlib
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/drone-deconfliction.git
cd drone-deconfliction
```

### 2. Install Requirements

Ensure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 3. Run the System

```bash
python main.py
```

---

## 📦 Example Output

### Console

```
[!] Conflict with drone_2 at distance 7.14m
    Times: (0, 10) vs (5, 15)
    Points: [50.0, 0.0, 0.0] ↔ [50.0, 0.0, 0.0]
```

### 3D Plot

- Each drone's mission is shown as a colored path
- Conflicts are drawn as **red lines** connecting closest points
- Waypoints marked with circles

---

## 📄 Sample Input Format

📍 `data/sample_missions.json`:

```json
[
  {
    "drone_id": "primary",
    "waypoints": [
      { "position": [0, 0, 0], "time": 0 },
      { "position": [100, 0, 0], "time": 10 },
      { "position": [100, 100, 0], "time": 20 }
    ]
  },
  {
    "drone_id": "drone_2",
    "waypoints": [
      { "position": [50, 50, 0], "time": 5 },
      { "position": [50, -50, 0], "time": 15 }
    ]
  }
]
```

Each waypoint includes:

- `position`: `[x, y, z]`
- `time`: when the drone should reach that point (seconds)

---

## ⚙️ Configuration

You can change:

- **Safety distance** in meters
- **Temporal overlap threshold**

📍 Inside `conflict_checker.py`:

```python
ConflictChecker(safety_distance=10.0, time_threshold=2.0)
```

---

## 🔍 How It Works

1. **Waypoint Segments**: Each mission is split into line segments between consecutive waypoints.
2. **3D Distance Check**: Minimum distance between each pair of segments is calculated using vector math.
3. **Time Check**: Conflicts are only flagged if the time intervals of the segments overlap.
4. **Visualization**: 3D plot with color-coded missions and highlighted conflict points.

---

## 📈 Future Extensions

- [ ] 4D animation (3D + time playback)
- [ ] REST API to serve as a live deconfliction service
- [ ] Integrate real-time drone telemetry (Kafka, MQTT)
- [ ] Use AI to auto-resolve conflicts (suggest alternate routes)

---

## 🧠 AI Integration

This solution was accelerated using:

- **ChatGPT**: math derivation, architectural guidance, and code templates
- **VS Code Insiders**: AI-assisted code navigation & refactoring

---

## 📌 License

This project is open for evaluation use. For commercial applications, please contact the author.

---

## 👨‍💻 Author

**Your Name**  
[LinkedIn](https://www.linkedin.com/in/yourname) | [GitHub](https://github.com/your-username)
