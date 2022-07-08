<p>Court is in session. We got a group of witnesses who have all taken an oath to tell the truth. The prosecutor is pointing at the defendants one by one and asking each witnesses a simple question - "guilty or not?". The witnesses are allowed to respond in one of the following three ways:</p>
<ul>
<li>I am sure he/she is guilty.</li>
<li>I am sure he/she is innocent.</li>
<li>I have no idea.</li>
</ul>
<p>The prosecutor has a hunch that one of the witnesses might not be telling the truth so she decides to cross-check all of their testimonies and see if the information gathered is consistent, i.e. there are no two witnesses <code>A</code> and <code>B</code> and a defendant <code>C</code> such that <code>A</code> says <code>C</code> is guilty while <code>B</code> says <code>C</code> is innocent.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>evidences = [[ 0, 1, 0, 1], 
             [-1, 1, 0, 0], 
             [-1, 0, 0, 1]]
</code></pre>
<p>the output should be<br />
<code>solution(evidences) = true</code>;</p>
</li>
<li>
<p>For</p>
<pre><code>evidences = [[ 1, 0], 
             [-1, 0], 
             [ 1, 1],
             [ 1, 1]]
</code></pre>
<p>the output should be<br />
<code>solution(evidences) = false</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer evidences</strong></p>
<p>2-dimensional array of integers representing the set of testimonials. <code>evidences[i][j]</code> is the testimonial of the <code>i<sup>th</sup></code> witness on the <code>j<sup>th</sup></code> defendant. <code>-1</code> means "innocent", <code>0</code> means "no idea", and <code>1</code> means "guilty".</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ evidences.length ≤ 5</code>,<br />
<code>2 ≤ evidences[0].length ≤ 10</code>,<br />
<code>evidences[i].length = evidences[j].length</code>,<br />
<code>-1 ≤ evidences[i][j] ≤ 1</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the evidence is consistent, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
