<p>You've been actively exchanging email with one of your colleagues and noticed that you can't open his attachments. Unfortunately, he's just went on a vacation and you need these attached files right now.</p>
<p>You've spent some time studying his emails and discovered that your colleague used the buggy email client which instead of using proper MIME <a href="https://en.wikipedia.org/wiki/Base64#MIME" target="_blank">Base64</a> encoding for the attachments used other variants differing in characters that represent values <code>62</code> and <code>63</code>.<br />
Furthermore, different versions of this email client used different variations of the encoding!</p>
<p>Given the <code>encoding</code> of the email client which was used to send <code>attachment</code>,<br />
decode it.</p>
<p>Here is the default Base64 encoding table:</p>
<table class="base64">
<tr><th class="Value">Value</th><th class="Char">Char</th><th class="Value">Value</th><th class="Char">Char</th><th class="Value">Value</th><th class="Char">Char</th><th class="Value">Value</th><th class="Char">Char</th>
</tr><tr><td class="Value">0</td><td class="Char">A</td><td class="Value">16</td><td class="Char">Q</td><td class="Value">32</td><td class="Char">g</td><td class="Value">48</td><td class="Char">w</td></tr>
<tr><td class="Value">1</td><td class="Char">B</td><td class="Value">17</td><td class="Char">R</td><td class="Value">33</td><td class="Char">h</td><td class="Value">49</td><td class="Char">x</td></tr>
<tr><td class="Value">2</td><td class="Char">C</td><td class="Value">18</td><td class="Char">S</td><td class="Value">34</td><td class="Char">i</td><td class="Value">50</td><td class="Char">y</td></tr>
<tr><td class="Value">3</td><td class="Char">D</td><td class="Value">19</td><td class="Char">T</td><td class="Value">35</td><td class="Char">j</td><td class="Value">51</td><td class="Char">z</td></tr>
<tr><td class="Value">4</td><td class="Char">E</td><td class="Value">20</td><td class="Char">U</td><td class="Value">36</td><td class="Char">k</td><td class="Value">52</td><td class="Char">0</td></tr>
<tr><td class="Value">5</td><td class="Char">F</td><td class="Value">21</td><td class="Char">V</td><td class="Value">37</td><td class="Char">l</td><td class="Value">53</td><td class="Char">1</td></tr>
<tr><td class="Value">6</td><td class="Char">G</td><td class="Value">22</td><td class="Char">W</td><td class="Value">38</td><td class="Char">m</td><td class="Value">54</td><td class="Char">2</td></tr>
<tr><td class="Value">7</td><td class="Char">H</td><td class="Value">23</td><td class="Char">X</td><td class="Value">39</td><td class="Char">n</td><td class="Value">55</td><td class="Char">3</td></tr>
<tr><td class="Value">8</td><td class="Char">I</td><td class="Value">24</td><td class="Char">Y</td><td class="Value">40</td><td class="Char">o</td><td class="Value">56</td><td class="Char">4</td></tr>
<tr><td class="Value">9</td><td class="Char">J</td><td class="Value">25</td><td class="Char">Z</td><td class="Value">41</td><td class="Char">p</td><td class="Value">57</td><td class="Char">5</td></tr>
<tr><td class="Value">10</td><td class="Char">K</td><td class="Value">26</td><td class="Char">a</td><td class="Value">42</td><td class="Char">q</td><td class="Value">58</td><td class="Char">6</td></tr>
<tr><td class="Value">11</td><td class="Char">L</td><td class="Value">27</td><td class="Char">b</td><td class="Value">43</td><td class="Char">r</td><td class="Value">59</td><td class="Char">7</td></tr>
<tr><td class="Value">12</td><td class="Char">M</td><td class="Value">28</td><td class="Char">c</td><td class="Value">44</td><td class="Char">s</td><td class="Value">60</td><td class="Char">8</td></tr>
<tr><td class="Value">13</td><td class="Char">N</td><td class="Value">29</td><td class="Char">d</td><td class="Value">45</td><td class="Char">t</td><td class="Value">61</td><td class="Char">9</td></tr>
<tr><td class="Value">14</td><td class="Char">O</td><td class="Value">30</td><td class="Char">e</td><td class="Value">46</td><td class="Char">u</td><td class="Value">62</td><td class="Char">+</td></tr>
<tr><td class="Value">15</td><td class="Char">P</td><td class="Value">31</td><td class="Char">f</td><td class="Value">47</td><td class="Char">v</td><td class="Value">63</td><td class="Char">/</td></tr>
</table>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>encoding = "-_"</code> and <code>message = "Q29kZVNpZ25hbA=="</code>, the output should be<br />
<code>solution(encoding, message) = "CodeSignal"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string encoding</strong></p>
<p>Two distinct characters used for values <code>62</code> and <code>63</code> instead of <code>+</code> and <code>/</code>.<br />
It's guaranteed that these characters are not equal to '=' or used for encoding values from <code>0</code> to <code>61</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>encoding.length = 2</code>,<br />
<code>encoding[0] ≠ encoding[1]</code>.</p>
</li>
<li>
<p><strong>[input] string message</strong></p>
<p>A message to decode.</p>
<p><em>Guaranteed constraints:</em><br />
<code>4 ≤ message.length ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A decoded message.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
