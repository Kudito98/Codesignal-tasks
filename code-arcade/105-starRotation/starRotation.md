<p>Consider a <code>(2k+1) × (2k+1)</code> square subarray of an integer integers matrix. Let's call the union of the square's two longest diagonals, middle column and middle row a <em>star</em>. Given the coordinates of the star's <code>center</code> in the <code>matrix</code> and its <code>width</code>, rotate it <code>45 · t</code> degrees clockwise preserving position of all matrix elements that do not belong to the <em>star</em>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>matrix = [[<b><font color="red">1</font></b>, 0, 0, <b><font color="red">2</font></b>, 0, 0, <b><font color="red">3</font></b>],
          [0, <b><font color="red">1</font></b>, 0, <b><font color="red">2</font></b>, 0, <b><font color="red">3</font></b>, 0],
          [0, 0, <b><font color="red">1</font></b>, <b><font color="red">2</font></b>, <b><font color="red">3</font></b>, 0, 0],
          [<b><font color="red">8</font></b>, <b><font color="red">8</font></b>, <b><font color="red">8</font></b>, <b><font color="red">9</font></b>, <b><font color="red">4</font></b>, <b><font color="red">4</font></b>, <b><font color="red">4</font></b>],
          [0, 0, <b><font color="red">7</font></b>, <b><font color="red">6</font></b>, <b><font color="red">5</font></b>, 0, 0],
          [0, <b><font color="red">7</font></b>, 0, <b><font color="red">6</font></b>, 0, <b><font color="red">5</font></b>, 0],
          [<b><font color="red">7</font></b>, 0, 0, <b><font color="red">6</font></b>, 0, 0, <b><font color="red">5</font></b>]]</code></pre>
<p><code>width = 7</code>, <code>center = [3, 3]</code>, and <code>t = 1</code>, the output should be</p>
<pre><code>solution(matrix, width, center, t) = [[<b><font color="red">8</font></b>, 0, 0, <b><font color="red">1</font></b>, 0, 0, <b><font color="red">2</font></b>],
                                          [0, <b><font color="red">8</font></b>, 0, <b><font color="red">1</font></b>, 0, <b><font color="red">2</font></b>, 0],
                                          [0, 0, <b><font color="red">8</font></b>, <b><font color="red">1</font></b>, <b><font color="red">2</font></b>, 0, 0],
                                          [<b><font color="red">7</font></b>, <b><font color="red">7</font></b>, <b><font color="red">7</font></b>, <b><font color="red">9</font></b>, <b><font color="red">3</font></b>, <b><font color="red">3</font></b>, <b><font color="red">3</font></b>],
                                          [0, 0, <b><font color="red">6</font></b>, <b><font color="red">5</font></b>, <b><font color="red">4</font></b>, 0, 0],
                                          [0, <b><font color="red">6</font></b>, 0, <b><font color="red">5</font></b>, 0, <b><font color="red">4</font></b>, 0],
                                          [<b><font color="red">6</font></b>, 0, 0, <b><font color="red">5</font></b>, 0, 0, <b><font color="red">4</font></b>]]</code></pre>
</li>
<li>
<p>For</p>
<pre><code>matrix = [[1, 0, 0, 2, <b><font color="red">0</font></b>, <b><font color="red">0</font></b>, <b><font color="red">3</font></b>],
          [0, 1, 0, 2, <b><font color="red">0</font></b>, <b><font color="red">3</font></b>, <b><font color="red">0</font></b>],
          [0, 0, 1, 2, <b><font color="red">3</font></b>, <b><font color="red">0</font></b>, <b><font color="red">0</font></b>],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0]]</code></pre>
<p><code>width = 3</code>, <code>center = [1, 5]</code>, and <code>t = 81</code>, the output should be</p>
<pre><code>solution(matrix, width, center, t) = [[1, 0, 0, 2, <b><font color="red">0</font></b>, <b><font color="red">0</font></b>, <b><font color="red">0</font></b>],
                                          [0, 1, 0, 2, <b><font color="red">3</font></b>, <b><font color="red">3</font></b>, <b><font color="red">3</font></b>],
                                          [0, 0, 1, 2, <b><font color="red">0</font></b>, <b><font color="red">0</font></b>, <b><font color="red">0</font></b>],
                                          [8, 8, 8, 9, 4, 4, 4],
                                          [0, 0, 7, 6, 5, 0, 0]]</code></pre>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p>A two-dimensional array of integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ matrix.length ≤ 15</code>,<br />
<code>3 ≤ matrix[i].length ≤ 15</code>,<br />
<code>matrix[i].length == matrix[j].length</code>,<br />
<code>0 ≤ matrix[i][j] ≤ 99</code>.</p>
</li>
<li>
<p><strong>[input] integer width</strong></p>
<p>An odd integer representing the star's width. It equals the length of the sides of the bounding square for the star.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ width ≤ min(matrix.length, matrix[i].length)</code>.</p>
</li>
<li>
<p><strong>[input] array.integer center</strong></p>
<p>An array of two integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>center.length = 2</code>,<br />
<code>(width - 1) / 2 ≤ center[0] &lt; matrix.length - (width - 1) / 2</code>,<br />
<code>(width - 1) / 2 ≤ center[1] &lt; matrix[i].length - (width - 1) / 2</code>.</p>
</li>
<li>
<p><strong>[input] integer t</strong></p>
<p>A non-negative integer denoting how many times the star should be rotated by 45 degrees.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ t ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>An array with specified <em>star</em> rotated by <code>45 · t</code> degrees.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
