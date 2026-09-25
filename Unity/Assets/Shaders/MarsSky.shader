// Gradient sky in the D12 palette: caramel zenith, dusty horizon (same colour as the fog), bluish sun halo.
Shader "Marte/Sky Gradient"
{
    Properties
    {
        _TopColor ("Zenith", Color) = (0.706, 0.533, 0.357, 1)
        _HorizonColor ("Horizon", Color) = (0.890, 0.769, 0.604, 1)
        _GroundColor ("Below horizon", Color) = (0.890, 0.769, 0.604, 1)
        _Exponent ("Horizon falloff", Range(0.2, 4)) = 0.8
        _SunColor ("Sun", Color) = (1, 0.97, 0.9, 1)
        _SunHaloColor ("Sun halo", Color) = (0.663, 0.776, 0.902, 1)
        _SunSize ("Sun size", Range(0.0005, 0.02)) = 0.0025
        _HaloSize ("Halo size", Range(1, 64)) = 10
    }
    SubShader
    {
        Tags { "Queue" = "Background" "RenderType" = "Background" "PreviewType" = "Skybox" }
        Cull Off ZWrite Off

        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"

            fixed4 _TopColor, _HorizonColor, _GroundColor, _SunColor, _SunHaloColor;
            half _Exponent, _SunSize, _HaloSize;

            struct v2f { float4 pos : SV_POSITION; float3 dir : TEXCOORD0; };

            v2f vert (appdata_base v)
            {
                v2f o;
                o.pos = UnityObjectToClipPos(v.vertex);
                o.dir = v.vertex.xyz;
                return o;
            }

            fixed4 frag (v2f i) : SV_Target
            {
                float3 d = normalize(i.dir);
                float3 col = d.y >= 0
                    ? lerp(_HorizonColor.rgb, _TopColor.rgb, pow(saturate(d.y), _Exponent))
                    : lerp(_HorizonColor.rgb, _GroundColor.rgb, saturate(-d.y * 8));

                float3 sunDir = normalize(_WorldSpaceLightPos0.xyz);
                float s = saturate(dot(d, sunDir));
                col = lerp(col, _SunHaloColor.rgb, pow(s, _HaloSize) * 0.6 * step(0, d.y));
                col += _SunColor.rgb * smoothstep(1 - _SunSize, 1 - _SunSize * 0.5, s);
                return fixed4(col, 1);
            }
            ENDCG
        }
    }
    Fallback Off
}
