<p>Once upon a time, in a kingdom far, far away, there lived a King Byteasar IV. His kingdom in the middle of a financial crisis, Byteasar was struggling to keep the economy out of a recession. Unfortunately there was not much he could do, and after much agonizing he came to the only solution: one of his cities had to be demolished, since keeping communication active between all the cities is way too expensive.</p>
<p>It is not yet known if Byteasar chose a city to destroy after careful planning or picked one at random. As a person with a PhD in History and Nobel prize in Computer Science, you can solve this mystery! Archaeologists have recently found a manuscript with information about the roads between the cities, that is now stored in the <code>roadRegister</code> matrix. You want to try and remove each city one by one and compare the road registers obtained this way. Thus you'll be able to compare the obtained roads and determine whether the one picked by Byteasar was the best by some criteria.</p>
<p>Given the <code>roadRegister</code>, return an array of all the road registers obtained after removing each of the cities one by one.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>roadRegister = [[false, true,  true,  false],
                [true,  false, true,  false],
                [true,  true,  false, true ],
                [false, false, true,  false]]
</code></pre>
<p>the output should be</p>
<pre><code>solution(roadRegister) = [
  [[false, true,  false],
   [true,  false, true ],
   [false, true,  false]],
  [[false, true,  false],
   [true,  false, true ],
   [false, true,  false]],
  [[false, true,  false],
   [true,  false, false],
   [false, false, false]],
  [[false, true,  true ],
   [true,  false, true ],
   [true,  true,  false]]
]
</code></pre>
<p>Here's the city connection that the given catalog represents:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/financialCrisis/img/initial.jpg?_tm=1624350032427" alt /></p>
<p>And here's how the cities are connected with one of the cities destroyed (cities <code>0</code> - <code>3</code>, respectively):<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/financialCrisis/img/deck.jpg?_tm=1624350032671" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean roadRegister</strong></p>
<p>Since cartography was not properly developed in the kingdom, the registers were used instead. A register is stored as a square matrix, with its size equal to the number of cities in the kingdom. If <code>roadRegister[i][j] = true</code>, then there is a road between the <code>i<sup>th</sup></code> and the <code>j<sup>th</sup></code> cities; the road doesn't exist otherwise.</p>
<p>It is guaranteed that there are no looping roads, i.e. roads that lead back to the same city it originated from.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ roadRegister.length ≤ 10</code>,<br />
<code>roadRegister[0].length = roadRegister.length</code>,<br />
<code>roadRegister[i][j] = roadRegister[j][i], i ≠ j</code>,<br />
<code>roadRegister[i][i] = false</code>.</p>
</li>
<li>
<p><strong>[output] array.array.array.boolean</strong></p>
<p>Array of the size <code>roadRegister.length</code>, with each of its elements of size <code>(roadRegister.length - 1) × (roadRegister.length - 1)</code>. The <code>i<sup>th</sup></code> element of the resulting array should contain the road register of the kingdom with the <code>i<sup>th</sup></code> city removed.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
