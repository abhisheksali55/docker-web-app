<svg width="860" viewBox="0 0 860 520" xmlns="http://www.w3.org/2000/svg" font-family="Arial, sans-serif">

  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>

    <!-- Animated dash styles -->
    <style>
      @keyframes flowR { from { stroke-dashoffset: 24; } to { stroke-dashoffset: 0; } }
      @keyframes flowD { from { stroke-dashoffset: 24; } to { stroke-dashoffset: 0; } }
      @keyframes flowL { from { stroke-dashoffset: 0; } to { stroke-dashoffset: 24; } }
      .aR { stroke-dasharray: 8 4; animation: flowR 0.6s linear infinite; }
      .aD { stroke-dasharray: 8 4; animation: flowD 0.6s linear infinite; }
      .aL { stroke-dasharray: 8 4; animation: flowL 0.6s linear infinite; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="860" height="520" fill="#ffffff" rx="16"/>

  <!-- Title -->
  <text x="430" y="38" text-anchor="middle" font-size="20" font-weight="bold" fill="#1a1a2e">CI/CD Pipeline</text>
  <text x="430" y="58" text-anchor="middle" font-size="12" fill="#666">Code commit se lekar live deployment tak</text>

  <!-- ═══ ROW 1 (left to right) ═══ -->

  <!-- Step 1: EC2 -->
  <rect x="30" y="90" width="110" height="75" rx="12" fill="#FFF3E0" stroke="#FF9900" stroke-width="1.5"/>
  <circle cx="48" cy="108" r="10" fill="#FF9900"/>
  <text x="48" y="112" text-anchor="middle" font-size="11" fill="white" font-weight="bold">1</text>
  <text x="85" y="118" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">Amazon</text>
  <text x="85" y="134" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">EC2</text>
  <text x="85" y="153" text-anchor="middle" font-size="10" fill="#BF360C">Code server</text>

  <!-- Arrow 1→2 -->
  <line class="aR" x1="142" y1="128" x2="178" y2="128" stroke="#FF9900" stroke-width="2" marker-end="url(#arr)"/>

  <!-- Step 2: GitHub -->
  <rect x="180" y="90" width="110" height="75" rx="12" fill="#F5F5F5" stroke="#333" stroke-width="1.5"/>
  <circle cx="198" cy="108" r="10" fill="#24292E"/>
  <text x="198" y="112" text-anchor="middle" font-size="11" fill="white" font-weight="bold">2</text>
  <text x="235" y="125" text-anchor="middle" font-size="13" font-weight="bold" fill="#24292E">GitHub</text>
  <text x="235" y="143" text-anchor="middle" font-size="10" fill="#555">Code push</text>
  <text x="235" y="157" text-anchor="middle" font-size="10" fill="#555">triggers pipeline</text>

  <!-- Arrow 2→3 -->
  <line class="aR" x1="292" y1="128" x2="328" y2="128" stroke="#555" stroke-width="2" marker-end="url(#arr)" style="animation-delay:0.15s"/>

  <!-- Step 3: Docker -->
  <rect x="330" y="90" width="110" height="75" rx="12" fill="#E3F2FD" stroke="#0db7ed" stroke-width="1.5"/>
  <circle cx="348" cy="108" r="10" fill="#0db7ed"/>
  <text x="348" y="112" text-anchor="middle" font-size="11" fill="white" font-weight="bold">3</text>
  <text x="385" y="125" text-anchor="middle" font-size="13" font-weight="bold" fill="#0277BD">Docker</text>
  <text x="385" y="143" text-anchor="middle" font-size="10" fill="#0277BD">Containerize</text>
  <text x="385" y="157" text-anchor="middle" font-size="10" fill="#0277BD">the app</text>

  <!-- Arrow 3→4 -->
  <line class="aR" x1="442" y1="128" x2="478" y2="128" stroke="#0db7ed" stroke-width="2" marker-end="url(#arr)" style="animation-delay:0.3s"/>

  <!-- Step 4: Docker Compose -->
  <rect x="480" y="90" width="120" height="75" rx="12" fill="#E3F2FD" stroke="#0db7ed" stroke-width="1.5" stroke-dasharray="6 3"/>
  <circle cx="498" cy="108" r="10" fill="#0db7ed"/>
  <text x="498" y="112" text-anchor="middle" font-size="11" fill="white" font-weight="bold">4</text>
  <text x="540" y="118" text-anchor="middle" font-size="13" font-weight="bold" fill="#0277BD">Docker</text>
  <text x="540" y="134" text-anchor="middle" font-size="13" font-weight="bold" fill="#0277BD">Compose</text>
  <text x="540" y="153" text-anchor="middle" font-size="10" fill="#0277BD">Multi-container</text>

  <!-- Arrow 4→5 -->
  <line class="aR" x1="602" y1="128" x2="638" y2="128" stroke="#0db7ed" stroke-width="2" marker-end="url(#arr)" style="animation-delay:0.45s"/>

  <!-- Step 5: Jenkins -->
  <rect x="640" y="90" width="110" height="75" rx="12" fill="#FFEBEE" stroke="#d33833" stroke-width="1.5"/>
  <circle cx="658" cy="108" r="10" fill="#d33833"/>
  <text x="658" y="112" text-anchor="middle" font-size="11" fill="white" font-weight="bold">5</text>
  <text x="695" y="125" text-anchor="middle" font-size="13" font-weight="bold" fill="#B71C1C">Jenkins</text>
  <text x="695" y="143" text-anchor="middle" font-size="10" fill="#B71C1C">CI/CD engine</text>
  <text x="695" y="157" text-anchor="middle" font-size="10" fill="#B71C1C">Auto-trigger</text>

  <!-- Arrow 5 → down (Jenkins to Shell) -->
  <line class="aD" x1="695" y1="167" x2="695" y2="283" stroke="#d33833" stroke-width="2" marker-end="url(#arr)" style="animation-delay:0.6s"/>

  <!-- ═══ ROW 2 (right to left) ═══ -->

  <!-- Step 6: Shell Script -->
  <rect x="640" y="285" width="110" height="75" rx="12" fill="#ECEFF1" stroke="#546E7A" stroke-width="1.5"/>
  <circle cx="658" cy="303" r="10" fill="#546E7A"/>
  <text x="658" y="307" text-anchor="middle" font-size="11" fill="white" font-weight="bold">6</text>
  <text x="695" y="320" text-anchor="middle" font-size="13" font-weight="bold" fill="#263238">Shell</text>
  <text x="695" y="336" text-anchor="middle" font-size="13" font-weight="bold" fill="#263238">Script</text>
  <text x="695" y="352" text-anchor="middle" font-size="10" fill="#546E7A">Runs build cmds</text>

  <!-- Arrow 6→7 (left) -->
  <line class="aL" x1="638" y1="323" x2="582" y2="323" stroke="#546E7A" stroke-width="2" marker-end="url(#arr)" style="animation-delay:0.75s"/>

  <!-- Step 7: Build Docker Image -->
  <rect x="470" y="285" width="130" height="75" rx="12" fill="#E3F2FD" stroke="#0db7ed" stroke-width="1.5"/>
  <circle cx="488" cy="303" r="10" fill="#0db7ed"/>
  <text x="488" y="307" text-anchor="middle" font-size="11" fill="white" font-weight="bold">7</text>
  <text x="535" y="316" text-anchor="middle" font-size="12" font-weight="bold" fill="#0277BD">Build Docker</text>
  <text x="535" y="332" text-anchor="middle" font-size="12" font-weight="bold" fill="#0277BD">Image</text>
  <text x="535" y="350" text-anchor="middle" font-size="10" fill="#0277BD">docker build -t app</text>

  <!-- Arrow 7→8 (left) -->
  <line class="aL" x1="468" y1="323" x2="412" y2="323" stroke="#0db7ed" stroke-width="2" marker-end="url(#arr)" style="animation-delay:0.9s"/>

  <!-- Step 8: Container Running -->
  <rect x="300" y="285" width="110" height="75" rx="12" fill="#E3F2FD" stroke="#0db7ed" stroke-width="2"/>
  <circle cx="318" cy="303" r="10" fill="#0db7ed"/>
  <text x="318" y="307" text-anchor="middle" font-size="11" fill="white" font-weight="bold">8</text>
  <text x="355" y="320" text-anchor="middle" font-size="13" font-weight="bold" fill="#0277BD">Container</text>
  <text x="355" y="336" text-anchor="middle" font-size="13" font-weight="bold" fill="#0277BD">Running</text>
  <text x="355" y="352" text-anchor="middle" font-size="10" fill="#0277BD">App is live! 🚀</text>

  <!-- Arrow 8 → Access label -->
  <line class="aL" x1="298" y1="323" x2="262" y2="323" stroke="#0db7ed" stroke-width="2" marker-end="url(#arr)" style="animation-delay:1.05s"/>

  <!-- Access the application label -->
  <text x="255" y="316" text-anchor="end" font-size="12" font-weight="bold" fill="#333">Access the</text>
  <text x="255" y="332" text-anchor="end" font-size="12" font-weight="bold" fill="#333">application</text>

  <!-- Arrow Access → Webhook -->
  <line class="aL" x1="148" y1="323" x2="142" y2="323" stroke="#555" stroke-width="2" marker-end="url(#arr)" style="animation-delay:1.2s"/>

  <!-- Step 9: Webhook / Users -->
  <rect x="30" y="285" width="110" height="75" rx="12" fill="#EDE7F6" stroke="#6c5ce7" stroke-width="1.5"/>
  <circle cx="48" cy="303" r="10" fill="#6c5ce7"/>
  <text x="48" y="307" text-anchor="middle" font-size="11" fill="white" font-weight="bold">9</text>
  <text x="85" y="320" text-anchor="middle" font-size="13" font-weight="bold" fill="#4527A0">Webhook</text>
  <text x="85" y="336" text-anchor="middle" font-size="13" font-weight="bold" fill="#4527A0">/ Users</text>
  <text x="85" y="352" text-anchor="middle" font-size="10" fill="#4527A0">Notified! ✅</text>

  <!-- ═══ Step descriptions box ═══ -->
  <rect x="30" y="395" width="800" height="105" rx="12" fill="#F8F9FA" stroke="#dee2e6" stroke-width="1"/>
  <text x="430" y="416" text-anchor="middle" font-size="12" font-weight="bold" fill="#333">📋 Step-by-step Flow</text>
  <text x="50" y="436" font-size="11" fill="#444">1. EC2 → Developer code yahan host karta hai</text>
  <text x="50" y="452" font-size="11" fill="#444">2. GitHub → Code push hote hi pipeline trigger</text>
  <text x="50" y="468" font-size="11" fill="#444">3. Docker → App containerize hoti hai</text>
  <text x="50" y="484" font-size="11" fill="#444">4. Docker Compose → Multi-container setup</text>
  <text x="50" y="500" font-size="11" fill="#444">5. Jenkins → CI/CD automation engine</text>
  <text x="440" y="436" font-size="11" fill="#444">6. Shell Script → Build commands automate</text>
  <text x="440" y="452" font-size="11" fill="#444">7. Build Docker Image → Latest image ready</text>
  <text x="440" y="468" font-size="11" fill="#444">8. Container Running → App live ho jaati hai</text>
  <text x="440" y="484" font-size="11" fill="#444">9. Webhook/Users → Notification + Access</text>

</svg>
