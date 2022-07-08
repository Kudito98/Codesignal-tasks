<p>During your most recent trip to Codelandia you decided to buy a brand new CodePlayer, a music player that (allegedly) can work with any possible media format. As it turns out, this isn't true: the player can't read lyrics written in the LRC format. It can, however, read the SubRip format, so now you want to translate all the lyrics you have from LRC to SubRip.</p>
<p>Since you are a pro programmer (no noob would ever get to Codelandia!), you're happy to implement a function that, given <code>lrcLyrics</code> and <code>songLength</code>, returns the lyrics in SubRip format.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>lrcLyrics = ["[00:12.00] Happy birthday dear coder,",
             "[00:17.20] Happy birthday to you!"]
</code></pre>
<p>and <code>songLength = "00:00:20"</code>, the output should be</p>
<pre><code>solution(lrcLyrics, songLength) = [
  "1",
  "00:00:12,000 --&gt; 00:00:17,200",
  "Happy birthday dear coder,",
  "",
  "2",
  "00:00:17,200 --&gt; 00:00:20,000",
  "Happy birthday to you!"
]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string lrcLyrics</strong></p>
<p>Lyrics in LRC format. Each string has the format <code>[MM:SS.xx] &lt;song_line&gt;</code>, (note the whitespace character after the time) where:</p>
<ul>
<li><code>MM:SS.xx</code> is the lyrics time (it is guaranteed that the elements of <code>lrcLyrics</code> are sorted in ascending order of this time);
<ul>
<li><code>0 ≤ int(xx) ≤ 99</code>;</li>
<li><code>0 ≤ int(SS) ≤ 59</code>;</li>
<li><code>0 ≤ int(MM) ≤ 99</code>;</li>
</ul>
</li>
<li><code>&lt;song_line&gt;</code> is the corresponding lyrics line.</li>
</ul>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ lrcLyrics.length ≤ 50</code>,<br />
<code>1 ≤ lrcLyrics[i].length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] string songLength</strong></p>
<p>The length of the song in the format <code>"HH:MM:SS"</code>. It is guaranteed that it is greater than the last time in <code>lrcLyrics</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ int(HH) ≤ 2</code>,<br />
<code>0 ≤ int(MM) ≤ 59</code>,<br />
<code>0 ≤ int(SS) ≤ 59</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>The given lyrics in the SubRip format. For each line in the <code>lrcLyrics</code>, three new lines should be generated:</p>
<ul>
<li>the first line is the 1-based lyrics line number;</li>
<li>the second line should be in the format <code>HH<sub>1</sub>:MM<sub>1</sub>:SS<sub>1</sub>,xxx<sub>1</sub> --&gt; HH<sub>2</sub>:MM<sub>2</sub>:SS<sub>2</sub>,xxx<sub>2</sub></code>, where:
<ul>
<li><code>HH<sub>1</sub>:MM<sub>1</sub>:SS<sub>1</sub>,xxx<sub>1</sub></code> the time the row starts;</li>
<li><code>HH<sub>2</sub>:MM<sub>2</sub>:SS<sub>2</sub>,xxx<sub>2</sub></code> when the next lyrics should appear, or the length of the song if it's the last lyrics line;</li>
</ul>
</li>
<li>the last line is the lyrics text itself.</li>
</ul>
<p>Each pair of consecutive three-lines groups should be separated by a single empty string.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
