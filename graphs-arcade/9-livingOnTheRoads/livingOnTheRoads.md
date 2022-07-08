<p>In a kingdom far, far away, there lives a King Byteasar IX. The history of the kingdom is rich with events and conflicts, most of which is focused on its cities. King Byteasar doesn't want to go down in history as a lame duck ruler, and especially doesn't want to have anything to do with the infamous cities of the kingdom.</p>
<p>Instead, king Byteasar wants to focus on the roads, which is why he issued a new decree: from now on, all roads are to be considered cities, and all cities are to be considered roads. Now his most grateful subjects must pack up their belongings and move out from the cities to the roads, and the cartographers are busy with building a new <code>roadRegister</code> of the kingdom. All roads of the kingdom are to be named for the cities they connect (i.e. <code>[<em>city<sub>1</sub></em>, <em>city<sub>2</sub></em>]</code>, <code><em>city<sub>1</sub></em> &lt; <em>city<sub>2</sub></em></code>), sorted <a href="keyword://lexicographical-order-for-arrays" target="_blank">lexicographically</a> and enumerated starting from <code>0</code>. A new road register for such a system needs to be created.</p>
<p>Your task is to help the cartographers build the new road register. Handle the challenge, and the glorious kingdom of Byteasar IX will never have to deal with its pesky cities ever again!</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>roadRegister = [
  [false, true,  true,  false, false, false],
  [true,  false, false, true,  false, false],
  [true,  false, false, false, false, false],
  [false, true,  false, false, false, false],
  [false, false, false, false, false, true ],
  [false, false, false, false, true,  false]
]
</code></pre>
<p>the output should be</p>
<pre><code>solution(roadRegister) = [
  [false, true,  true,  false],
  [true,  false, false, false],
  [true,  false, false, false],
  [false, false, false, false]
]
</code></pre>
<p>Here's how the new register can be obtained:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/livingOnTheRoads/img/example.jpg?_tm=1624348813381" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean roadRegister</strong></p>
<p>Since cartography has not yet been properly developed in the kingdom, the registers are used instead. A register is stored as a square matrix, with its size equal to the number of cities in the kingdom. If <code>roadRegister[i][j] = true</code>, then there is a road between the <code>i<sup>th</sup></code> and the <code>j<sup>th</sup></code> cities; the road doesn't exist otherwise.</p>
<p>It is guaranteed that there are no looping roads, i.e. roads that lead back to the same city it originated from.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ roadRegister.length ≤ 15</code>,<br />
<code>roadRegister[0].length = roadRegister.length</code>,<br />
<code>roadRegister[i][j] = roadRegister[j][i], i ≠ j</code>,<br />
<code>roadRegister[i][i] = false</code>.</p>
</li>
<li>
<p><strong>[output] array.array.boolean</strong></p>
<p>The <code>roadRegister</code> after all cities are turned into roads, and vice versa.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
