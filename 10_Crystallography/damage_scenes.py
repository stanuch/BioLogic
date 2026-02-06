from pymol import cmd

def make_damage_scenes(sel_name, obj_name, map_2fofc, map_fofc, around=5.0, level_2fofc=1.0, level_fofc=3.0):
    
    model = cmd.get_model(sel_name)
    seen = set()
    idx = 1
    
    for at in model.atom:
        key = (at.segi, at.chain, at.resi, at.resn)
        if key in seen:
            continue
        seen.add(key)
        sele = f"/{obj_name}//{at.chain}/{at.resi}/"
        
        cmd.hide("everything")
        cmd.show("cartoon", obj_name)
        cmd.show("sticks", sele)
        cmd.util.cnc(sele) 
        cmd.zoom(sele, around)
        
        m2_name = f"m2_{obj_name}_{idx}"
        mfn_name = f"mfn_{obj_name}_{idx}"
        mfp_name = f"mfp_{obj_name}_{idx}"

        cmd.isomesh(m2_name, map_2fofc, level_2fofc, sele, carve=around)
        cmd.color("forest", m2_name)
        
        cmd.isomesh(mfn_name, map_fofc, -level_fofc, sele, carve=around)
        cmd.color("red", mfn_name)
        
        cmd.isomesh(mfp_name, map_fofc, level_fofc, sele, carve=around)
        cmd.color("blue", mfp_name)

        scene_name = f"dmg_{obj_name}_{at.resn}_{at.resi}"
        cmd.scene(scene_name, "store")
        print(f"Zapisano scenę: {scene_name}")
        idx += 1

cmd.extend("make_damage_scenes", make_damage_scenes)