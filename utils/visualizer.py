import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_missions(missions, conflicts):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    colors = ['blue', 'green', 'orange', 'purple', 'cyan']

    for idx, mission in enumerate(missions):
        xs = [w.x for w in mission.waypoints]
        ys = [w.y for w in mission.waypoints]
        zs = [w.z for w in mission.waypoints]
        ax.plot(xs, ys, zs, marker='o', label=f'Drone {mission.drone_id}', color=colors[idx % len(colors)])

    for c in conflicts:
        px, py, pz = c['point_on_primary']
        qx, qy, qz = c['point_on_other']
        ax.plot([px, qx], [py, qy], [pz, qz], color='red', linewidth=2, label='Conflict')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Drone Mission Conflict Visualization')
    ax.legend()
    plt.tight_layout()
    plt.show()
