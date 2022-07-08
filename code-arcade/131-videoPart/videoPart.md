<p>You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have already watched.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>part = "02:20:00"</code> and <code>total = "07:00:00"</code>, the output should be<br />
<code>solution(part, total) = [1, 3]</code>.</p>
<p>You have watched <code>1 / 3</code> of the whole video.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string part</strong></p>
<p>A string of the following format <code>"hh:mm:ss"</code> representing the time you have been watching the video.</p>
</li>
<li>
<p><strong>[input] string total</strong></p>
<p>A string of the following format <code>"hh:mm:ss"</code> representing the total video duration.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>An array of the following format <code>[a, b]</code> (where <code>a / b</code> is <a href="keyword://reduced-fraction" target="_blank">a reduced fraction</a>).</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
