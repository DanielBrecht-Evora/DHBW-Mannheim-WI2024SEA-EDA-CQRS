# ============================================
# Lightbulb Control System
# Project by Daniel and Leonie
# ============================================

COLORS = {
    'r': 'red',
    'g': 'green',
    'b': 'blue',
    'y': 'yellow',
    'w': 'white'
}

def display_menu():
    print("\n" + "="*50)
    print("Project from Daniel and Leonie: {\"Die Erleuchtung\"}")
    print("="*50)
    
    print("\n📋 Commands & Queries")
    print("-" * 50)
    
    print("\n🎨 Change Color:")
    for code, color in COLORS.items():
        print(f"  {code} = {color}")
    
    print("\n⚙️  Other Options:")
    print("  ?    = Show current color")
    print("  esc  = Exit program")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    display_menu()