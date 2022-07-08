<p>You're a pretty busy billionaire, and you often fly your personal Private Jet to remote places. Usually travel doesn't bother you, but this time you are unlucky: it's New Year's Eve, and since you have to fly halfway around the world, you'll probably have to celebrate New Year's Day in mid-air!</p>
<p>Your course lies west of your current location and crosses several time zones. The pilot told you the exact schedule: it is known that you will take off at <code>takeOffTime</code>, and in <code>minutes[i]</code> after takeoff you will cross the <code>i<sup>th</sup></code> border between time zones. After crossing each border you will have to set your wrist watch one hour earlier (every second matters to you, so you can't let your watch show incorrect time). It is guaranteed that you won't cross the <a href="https://en.wikipedia.org/wiki/International_Date_Line" target="_blank">IDL</a> (i.e. after crossing each time zone border your current time will be set one hour back).</p>
<p>You've been thinking about this situation and realized that it might be a good opportunity to celebrate New Year's Day more than once, i.e. each time your wrist watch shows <code>00:00</code>. Assuming that you set your watch immediately after the border is crossed, how many times will you be able to celebrate this New Year's Day with a nice bottle of champagne? Note that the answer should include celebrations both in mid-air and on the ground (it doesn't matter if the plane landed in the last time zone before the midnight or not, you'll not let the last opportunity to celebrate New Year slip through your fingers).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>takeOffTime = "23:35"</code> and <code>minutes = [60, 90, 140]</code>,<br />
the output should be<br />
<code>solution(takeOffTime, minutes) = 3</code>.</p>
<p>Here is the list of events by the time zones:</p>
<ul>
<li><strong>initial time zone:</strong>
<ul>
<li>at <code>23:35</code> your flight starts;</li>
<li>at <code>00:00</code> you celebrate New Year for the first time;</li>
<li>at <code>00:35</code> (<code>60</code> minutes after the take off) you cross the first border;</li>
</ul>
</li>
<li><strong>time zone -1:</strong>
<ul>
<li>at <code>23:35</code> you cross the border (<code>00:35</code> by your initial time zone);</li>
<li>at <code>00:00</code> you celebrate New Year for the second time (<code>01:00</code> by your initial time zone);</li>
<li>at <code>00:05</code> (<code>90</code> minutes after the take off) you cross the second border;</li>
</ul>
</li>
<li><strong>time zone -2:</strong>
<ul>
<li>at <code>23:05</code> you cross the border;</li>
<li>at <code>23:55</code> (<code>140</code> minutes after the take off) you cross another border;</li>
</ul>
</li>
<li><strong>time zone -3:</strong>
<ul>
<li>at <code>22:55</code> you cross the border;</li>
<li>at <code>00:00</code> you celebrate New Year for the third time.</li>
</ul>
</li>
</ul>
<p>Thus, the output should be <code>3</code>. That's a lot of champagne!</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string takeOffTime</strong></p>
<p>The take off time in the 24-hour format <code>"HH:MM"</code>. It is guaranteed that the given time is valid. The <code>"00:00"</code> time corresponds to the midnight of 31<sup>st</sup> of December / 1<sup>st</sup> of January.</p>
<p><em>Guaranteed constraints:</em><br />
<code>"00" ≤ HH ≤ "23"</code>,<br />
<code>"00" ≤ MM ≤ "59"</code>.</p>
</li>
<li>
<p><strong>[input] array.integer minutes</strong></p>
<p>A strictly increasing array of integers. <code>minutes[i]</code> stands for the number of minutes from the take off to crossing the <code>i<sup>th</sup></code> time zone border.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ minutes.length ≤ 20</code>,<br />
<code>1 ≤ minutes[i] ≤ 1500</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of times you will be able to celebrate New Year's Day.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
