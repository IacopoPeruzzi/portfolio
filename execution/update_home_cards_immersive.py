import os

def update_file(path, is_grid_2=True):
    with open(path, "r") as f:
        content = f.read()
    
    # Replacing the card rendering logic
    import re
    
    # Define the new card structure
    new_card_jsx = '''
            <Link key={item.id} to={`/case-study/${item.id}`} className="card reveal">
              {item.heroImage && (
                <div className="card-bg">
                  <img src={item.heroImage} alt={item.title} />
                  <div className="card-overlay"></div>
                </div>
              )}
              <div className="card-content">
                <h3 style={{fontSize: '2rem'}}>{item.title}</h3>
                <p style={{fontSize: '1.1rem'}}>{item.subtitle}</p>
                <div className="tag-list">
                  {item.tags.slice(0, 3).map(t => <span key={t} className="tag">{t}</span>)}
                </div>
              </div>
            </Link>
    '''
    
    # For StrategicInitiatives (grid-2)
    content = re.sub(r'<Link key={item.id} to={`/case-study/\${item.id}`}.*?</Link>', new_card_jsx, content, flags=re.DOTALL)
    
    # For ClientProjects (grid-3, different variable name 'p')
    new_card_p_jsx = new_card_jsx.replace('item.', 'p.')
    content = re.sub(r'<Link key={p.id} to={`/case-study/\${p.id}`}.*?</Link>', new_card_p_jsx, content, flags=re.DOTALL)

    with open(path, "w") as f:
        f.write(content)

# Apply to both
base_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components/"
update_file(base_path + "StrategicInitiatives.jsx")
update_file(base_path + "ClientProjects.jsx", is_grid_2=False)

print("Home cards updated to immersive full-background style!")
