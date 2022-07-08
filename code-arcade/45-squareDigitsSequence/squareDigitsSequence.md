<p>Consider a sequence of numbers <code>a<sub>0</sub></code>, <code>a<sub>1</sub></code>, ..., <code>a<sub>n</sub></code>, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.</p>
<p>Given the first element <code>a0</code>, find the length of the sequence.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>a0 = 16</code>, the output should be<br />
<code>solution(a0) = 9</code>.</p>
<p>Here's how elements of the sequence are constructed:</p>
<ul>
<li><code>a<sub>0</sub> = 16</code></li>
<li><code>a<sub>1</sub> = 1<sup>2</sup> + 6<sup>2</sup> = 37</code></li>
<li><code>a<sub>2</sub> = 3<sup>2</sup> + 7<sup>2</sup> = 58</code></li>
<li><code>a<sub>3</sub> = 5<sup>2</sup> + 8<sup>2</sup> = 89</code></li>
<li><code>a<sub>4</sub> = 8<sup>2</sup> + 9<sup>2</sup> = 145</code></li>
<li><code>a<sub>5</sub> = 1<sup>2</sup> + 4<sup>2</sup> + 5<sup>2</sup> = 42</code></li>
<li><code>a<sub>6</sub> = 4<sup>2</sup> + 2<sup>2</sup> = 20</code></li>
<li><code>a<sub>7</sub> = 2<sup>2</sup> + 0<sup>2</sup> = 4</code></li>
<li><code>a<sub>8</sub> = 4<sup>2</sup> = 16</code>, which has already occurred before (<code>a<sub>0</sub></code>)</li>
</ul>
<p>Thus, there are <code>9</code> elements in the sequence.</p>
</li>
<li>
<p>For <code>a0 = 103</code>, the output should be<br />
<code>solution(a0) = 4</code>.</p>
<p>The sequence goes as follows: <code>103 -&gt; 10 -&gt; 1 -&gt; 1</code>, <code>4</code> elements altogether.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer a0</strong></p>
<p>First element of a sequence, positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a0 ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
