using System;
using UnityEngine;

namespace Marte.World
{
    // A named place on the map (design/proposta-marcos-e-cavernas.md). Position is the true map position
    // (origin at the map center) with y on the terrain surface.
    [Serializable]
    public struct Landmark
    {
        public string id;
        public int number;            // 0 = unnumbered (base, start, trail start...)
        public string name;
        public string type;           // caverna|mesa|real|historia|recurso|formacao|mirante|base|inicio
        public string origin;         // real|real+jogo|inspirado_no_real|jogo
        public string cave;           // cave subtype, empty when there is none
        public string ice;
        public bool visibleFromFar;
        public string description;
        public Vector3 position;
    }
}
