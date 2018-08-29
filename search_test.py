from main import scanner


testText = '''UTF8 DATATON_DFC_DATA_590925_620721_AUC069 {
	"Structure and File Format (C) Copyright Dataton AB" 2017 1
	"WATCHMAKER" 6 2 2 0
	ObjTransferable ObjTransferable struct extends {
		TextTransferable struct extends {
			Transferable struct {
			}
		} {
		}
	} {
		mObjData list object true,
		mClassName string
	} {
		{ // mObjData
			TimelineTask struct extends {
				Task struct extends {
					TaskListItem struct {
						mTaskNum int
					}
				} {
					mTrigger Expression struct {
						mItems list ExprItem struct {
						} true
					}
				}
			} {
				mAction reference AuxTimeline struct extends {
					Timeline struct extends {
						VisibleMedia struct extends {
							Media struct extends {
								MediaListItem struct {
								}
							} {
								mFile MediaFile struct {
									mPath string,
									mFileSize int,
									mModDate int,
									mHasURL bool,
									mIsProxy bool,
									mNoDownload bool,
									mAutoRefresh bool
								},
								mStagePreview bool
							}
						} {
							mDim IDimension struct extends {
								iPDBase struct {
									x int,
									y int
								}
							} {
							},
							mAlphaMode AlphaMode enum {
								KAMUnknown 0,
								KAMNoAlpha 1,
								KAMStraight 2,
								KAMPreWhite 3,
								KAMPreBlack 4
							},
							mForcedAlphaMode AlphaMode,
							mSuppressThumbnail bool
						}
					} {
						mName string,
						mLayers list Layer struct {
							mName string,
							mCues list Cue struct {
								mTime TimeRange struct {
									MStart time,
									MDuration time
								},
								mCueID int
							} true,
							mExpanded bool,
							mIndex int,
							mConditional int,
							mDisabled bool,
							mStandBy StandByMode enum {
								kSB_Normal 0,
								kSB_StandBy 1,
								kSB_Both 2
							},
							mLocked bool,
							mSpecLevels bool,
							mLevels int
						} false,
						mCurrLayerIndex int,
						mTimeScale int,
						mDuration time,
						mCueIDSeed int,
						mFrontmostAtTop bool,
						MWinState TimelineWinState struct extends {
							WinState struct {
								mState State enum {
									kWS_NotShown 0,
									kWS_Iconized 1,
									kWS_Normal 2,
									kWS_ZoomedFull 3
								},
								mLeft int,
								mTop int,
								mWidth int,
								mHeight int,
								mActive bool
							}
						} {
							MSashPos int,
							MHdrWidth int,
							MVScrollPos int
						},
						mFixedDuration bool,
						mSpecTiers bool,
						mTiers int
					}
				} {
					mAlwaysOnTop StackingOrder enum {
						kTaskListOrder 0,
						kOnTop 1,
						kAboveEdgeBlend 2
					}
				} false
			} {
				0, // mTaskNum
				{ // mTrigger
					{ // mItems
					}
				},
				{ // mAction
					{ "", 0, 0, false, false, false, false }, // mFile mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
					true, // mStagePreview
					{ 0, 0 }, // mDim x y
					0, // mAlphaMode
					0, // mForcedAlphaMode
					false, // mSuppressThumbnail
					"Timeline 41", // mName
					{ // mLayers
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							1, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							2, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							3, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						}
					},
					1, // mCurrLayerIndex
					50, // mTimeScale
					10:00.0, // mDuration
					0, // mCueIDSeed
					true, // mFrontmostAtTop
					{ 0, 0, 0, 0, 0, false, 0, 0, 0 }, // MWinState mState mLeft mTop mWidth mHeight mActive MSashPos MHdrWidth MVScrollPos
					false, // mFixedDuration
					false, // mSpecTiers
					0, // mTiers
					0 // mAlwaysOnTop
				}
			},
			TimelineTask {
				0, // mTaskNum
				{ // mTrigger
					{ // mItems
					}
				},
				{ // mAction
					{ "", 0, 0, false, false, false, false }, // mFile mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
					true, // mStagePreview
					{ 0, 0 }, // mDim x y
					0, // mAlphaMode
					0, // mForcedAlphaMode
					false, // mSuppressThumbnail
					"Timeline 42", // mName
					{ // mLayers
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							1, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							2, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
								ContMediaCue struct extends {
									MediaCue struct extends {
										MediaCueBase struct extends {
											TweeningCue struct extends {
												Cue
											} {
											}
										} {
											mMedia reference Media true
										}
									} {
										mPreroll time,
										mParams list TweenParam struct {
										} true,
										mPreviewQuality PreviewQuality enum {
											kPQ_Best 0,
											kPQ_Reduced 1,
											kPQ_None 2
										},
										mInitialPos Point3D struct extends {
											_pvs3DBase struct {
												x float,
												y float,
												z float
											}
										} {
										},
										mOrientAlongPath bool,
										mRenderAsMaskOnly bool,
										mMask Masking enum {
											kMM_None 0,
											kMM_Alpha 1,
											kMM_AlphaInv 2,
											kMM_Luma 3,
											kMM_LumaInv 4
										},
										mBlend Blending enum {
											kBM_Normal 0,
											kBM_Add 1,
											kBM_Multiply 2,
											kBM_Screen 3,
											kBM_Lighten 4,
											kBM_Darken 5,
											kBM_Linear_Burn 6
										},
										mExplicitTarget bool,
										mPlayThroughDisplay reference StageItem struct extends {
											StageListItem struct {
											}
										} {
											mName string,
											mLoc IPoint struct extends {
												iPDBase
											} {
											},
											mAddress string,
											mPrimary bool,
											mEnabled bool,
											mDialogState ModelessDialogState struct extends {
												WinState
											} {
												mLastTab int,
												mNotebook string
											}
										} true,
										mShader reference SCProxy struct {
											mRecipe ShaderRecipe struct {
												mIdentifiers string,
												mNumbIdentifiers int,
												mHash int
											}
										} false,
										mStacking ZOrder enum {
											kZO_Default 0,
											kZO_ByLayer 1,
											kZO_ByDepth 2
										},
										mOrientation FwdMotion enum {
											kFM_XPlus 0,
											kFM_XMinus 1,
											kFM_YPlus 2,
											kFM_YMinus 3,
											kFM_ZPlus 4,
											kFM_ZMinus 5
										},
										mLocalVanishingPoint bool,
										mInteractive string,
										mExtTransform bool
									}
								} {
									mInTime time,
									mLooping bool,
									mFreeRunning bool,
									mTimeScalePercentage int,
									mExpectedAlphaMode AlphaMode,
									mOutputAssignments array 8 int,
									mChannelMapping array 576 int
								} {
									{ 13.3, 59.993 }, // mTime MStart MDuration
									1, // mCueID
									VideoMedia struct extends { // mMedia
										VisibleMedia
									} {
										mIsPreSplit bool,
										mIsStereoscopic bool,
										mIsImageSequence bool,
										mDuration time,
										mUsePreviewMovie bool,
										mPreviewMovie MediaFile,
										mMultiFileExt string,
										mAllowHardwareAcc bool,
										mDoFrameBlend bool,
										mFrameRate float,
										mIsBaseName string,
										mIsFirstSeqNumber int,
										mIsNumberOfFiles int,
										mIsNumberOfDigits int,
										mAudioNumOutput int,
										mIsExtension string,
										mDdsFlavour DdsFlavour enum {
											kDF_None 0,
											kDF_DXT1 1,
											kDF_DXT5 2,
											kDF_RGBA 3
										}
									} #1586 {
										{ "/C:/Users/timsf/OneDrive/Documents/Watchout/Watchout 2016 MEDIA/NFL CFB MEDIA/N" // mFile mPath
											"231_NFT_GENERIC_BACKWALL_top_v3.mp4", 152403992, 1504869486, false, false, false, false }, // mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										true, // mStagePreview
										{ 1920, 1080 }, // mDim x y
										1, // mAlphaMode
										0, // mForcedAlphaMode
										false, // mSuppressThumbnail
										false, // mIsPreSplit
										false, // mIsStereoscopic
										false, // mIsImageSequence
										59.993, // mDuration
										false, // mUsePreviewMovie
										{ "", 0, 0, false, false, false, false }, // mPreviewMovie mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										"", // mMultiFileExt
										true, // mAllowHardwareAcc
										true, // mDoFrameBlend
										1, // mFrameRate
										"", // mIsBaseName
										0, // mIsFirstSeqNumber
										1, // mIsNumberOfFiles
										1, // mIsNumberOfDigits
										2, // mAudioNumOutput
										"", // mIsExtension
										0 // mDdsFlavour
									},
									0.0, // mPreroll
									{ // mParams
										AnchorTweenPointQuad struct extends {
											_tweenPointQP struct extends {
												_quadTweenPoint struct extends {
													TweenPoint struct extends {
														TweenParam
													} {
														mTimePos float
													}
												} {
													mSmooth bool
												}
											} {
												mValue Point3D
											}
										} {
										} {
											0, // mTimePos
											false, // mSmooth
											{ 960, 540, 0 } // mValue x y z
										}
									},
									0, // mPreviewQuality
									{ 5660, 1940, 0 }, // mInitialPos x y z
									false, // mOrientAlongPath
									false, // mRenderAsMaskOnly
									0, // mMask
									0, // mBlend
									false, // mExplicitTarget
									#0, // mPlayThroughDisplay
									#0, // mShader
									0, // mStacking
									0, // mOrientation
									false, // mLocalVanishingPoint
									"", // mInteractive
									false, // mExtTransform
									0.0, // mInTime
									false, // mLooping
									false, // mFreeRunning
									100, // mTimeScalePercentage
									1, // mExpectedAlphaMode
									{ // mOutputAssignments
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0
									},
									{ // mChannelMapping
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1
									}
								}
							},
							false, // mExpanded
							3, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						}
					},
					1, // mCurrLayerIndex
					50, // mTimeScale
					10:00.0, // mDuration
					1, // mCueIDSeed
					true, // mFrontmostAtTop
					{ 0, 0, 0, 0, 0, false, 0, 0, 0 }, // MWinState mState mLeft mTop mWidth mHeight mActive MSashPos MHdrWidth MVScrollPos
					false, // mFixedDuration
					false, // mSpecTiers
					0, // mTiers
					0 // mAlwaysOnTop
				}
			},
			TimelineTask {
				0, // mTaskNum
				{ // mTrigger
					{ // mItems
					}
				},
				{ // mAction
					{ "", 0, 0, false, false, false, false }, // mFile mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
					true, // mStagePreview
					{ 0, 0 }, // mDim x y
					0, // mAlphaMode
					0, // mForcedAlphaMode
					false, // mSuppressThumbnail
					"Timeline 43", // mName
					{ // mLayers
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							1, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							2, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							3, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						}
					},
					1, // mCurrLayerIndex
					50, // mTimeScale
					10:00.0, // mDuration
					0, // mCueIDSeed
					true, // mFrontmostAtTop
					{ 0, 0, 0, 0, 0, false, 0, 0, 0 }, // MWinState mState mLeft mTop mWidth mHeight mActive MSashPos MHdrWidth MVScrollPos
					false, // mFixedDuration
					false, // mSpecTiers
					0, // mTiers
					0 // mAlwaysOnTop
				}
			},
			TimelineTask {
				0, // mTaskNum
				{ // mTrigger
					{ // mItems
					}
				},
				{ // mAction
					{ "", 0, 0, false, false, false, false }, // mFile mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
					true, // mStagePreview
					{ 0, 0 }, // mDim x y
					0, // mAlphaMode
					0, // mForcedAlphaMode
					false, // mSuppressThumbnail
					"Timeline 44", // mName
					{ // mLayers
						{
							"", // mName
							{ // mCues
								ContMediaCue {
									{ 1.2, 1:00.011 }, // mTime MStart MDuration
									1, // mCueID
									VideoMedia #3083 { // mMedia
										{ "/C:/Users/timsf/OneDrive/Documents/Watchout/Watchout 2017 MEDIA/NFL CFB MEDIA B" // mFile mPath
											"IN/BTM-HOLIDAY_SKYLINE_02_1223.mp4", 153958756, 1482524071, false, false, false, false }, // mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										true, // mStagePreview
										{ 1920, 1080 }, // mDim x y
										1, // mAlphaMode
										0, // mForcedAlphaMode
										false, // mSuppressThumbnail
										false, // mIsPreSplit
										false, // mIsStereoscopic
										false, // mIsImageSequence
										1:00.011, // mDuration
										false, // mUsePreviewMovie
										{ "", 0, 0, false, false, false, false }, // mPreviewMovie mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										"", // mMultiFileExt
										true, // mAllowHardwareAcc
										true, // mDoFrameBlend
										1, // mFrameRate
										"", // mIsBaseName
										0, // mIsFirstSeqNumber
										1, // mIsNumberOfFiles
										1, // mIsNumberOfDigits
										2, // mAudioNumOutput
										"", // mIsExtension
										0 // mDdsFlavour
									},
									0.0, // mPreroll
									{ // mParams
										AnchorTweenPointQuad {
											0, // mTimePos
											false, // mSmooth
											{ 960, 540, 0 } // mValue x y z
										}
									},
									0, // mPreviewQuality
									{ 5660, 1940, 0 }, // mInitialPos x y z
									false, // mOrientAlongPath
									false, // mRenderAsMaskOnly
									0, // mMask
									0, // mBlend
									false, // mExplicitTarget
									#0, // mPlayThroughDisplay
									#0, // mShader
									0, // mStacking
									0, // mOrientation
									false, // mLocalVanishingPoint
									"", // mInteractive
									false, // mExtTransform
									0.0, // mInTime
									false, // mLooping
									false, // mFreeRunning
									100, // mTimeScalePercentage
									1, // mExpectedAlphaMode
									{ // mOutputAssignments
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0
									},
									{ // mChannelMapping
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1
									}
								}
							},
							false, // mExpanded
							1, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							2, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							3, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						}
					},
					3, // mCurrLayerIndex
					200, // mTimeScale
					10:00.0, // mDuration
					1, // mCueIDSeed
					true, // mFrontmostAtTop
					{ 0, 0, 0, 0, 0, false, 0, 0, 0 }, // MWinState mState mLeft mTop mWidth mHeight mActive MSashPos MHdrWidth MVScrollPos
					false, // mFixedDuration
					false, // mSpecTiers
					0, // mTiers
					0 // mAlwaysOnTop
				}
			},
			TimelineTask {
				0, // mTaskNum
				{ // mTrigger
					{ // mItems
					}
				},
				{ // mAction
					{ "", 0, 0, false, false, false, false }, // mFile mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
					true, // mStagePreview
					{ 0, 0 }, // mDim x y
					0, // mAlphaMode
					0, // mForcedAlphaMode
					false, // mSuppressThumbnail
					"Timeline 45", // mName
					{ // mLayers
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							1, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							2, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							3, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						}
					},
					1, // mCurrLayerIndex
					50, // mTimeScale
					10:00.0, // mDuration
					0, // mCueIDSeed
					true, // mFrontmostAtTop
					{ 0, 0, 0, 0, 0, false, 0, 0, 0 }, // MWinState mState mLeft mTop mWidth mHeight mActive MSashPos MHdrWidth MVScrollPos
					false, // mFixedDuration
					false, // mSpecTiers
					0, // mTiers
					0 // mAlwaysOnTop
				}
			},
			TimelineTask {
				0, // mTaskNum
				{ // mTrigger
					{ // mItems
					}
				},
				{ // mAction
					{ "", 0, 0, false, false, false, false }, // mFile mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
					true, // mStagePreview
					{ 0, 0 }, // mDim x y
					0, // mAlphaMode
					0, // mForcedAlphaMode
					false, // mSuppressThumbnail
					"Timeline 46", // mName
					{ // mLayers
						{
							"", // mName
							{ // mCues
								ContMediaCue {
									{ 1.1, 1:00.011 }, // mTime MStart MDuration
									1, // mCueID
									#3083, // mMedia
									0.0, // mPreroll
									{ // mParams
										AnchorTweenPointQuad {
											0, // mTimePos
											false, // mSmooth
											{ 960, 540, 0 } // mValue x y z
										}
									},
									0, // mPreviewQuality
									{ 5660, 1940, 0 }, // mInitialPos x y z
									false, // mOrientAlongPath
									false, // mRenderAsMaskOnly
									0, // mMask
									0, // mBlend
									false, // mExplicitTarget
									#0, // mPlayThroughDisplay
									#0, // mShader
									0, // mStacking
									0, // mOrientation
									false, // mLocalVanishingPoint
									"", // mInteractive
									false, // mExtTransform
									0.0, // mInTime
									false, // mLooping
									false, // mFreeRunning
									100, // mTimeScalePercentage
									1, // mExpectedAlphaMode
									{ // mOutputAssignments
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0
									},
									{ // mChannelMapping
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1
									}
								}
							},
							false, // mExpanded
							1, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							2, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							3, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						}
					},
					3, // mCurrLayerIndex
					50, // mTimeScale
					10:00.0, // mDuration
					1, // mCueIDSeed
					true, // mFrontmostAtTop
					{ 0, 0, 0, 0, 0, false, 0, 0, 0 }, // MWinState mState mLeft mTop mWidth mHeight mActive MSashPos MHdrWidth MVScrollPos
					false, // mFixedDuration
					false, // mSpecTiers
					0, // mTiers
					0 // mAlwaysOnTop
				}
			},
			TimelineTask {
				0, // mTaskNum
				{ // mTrigger
					{ // mItems
					}
				},
				{ // mAction
					{ "", 0, 0, false, false, false, false }, // mFile mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
					true, // mStagePreview
					{ 0, 0 }, // mDim x y
					0, // mAlphaMode
					0, // mForcedAlphaMode
					false, // mSuppressThumbnail
					"Timeline 47", // mName
					{ // mLayers
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							1, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
								ContMediaCue {
									{ 2.0, 30.03 }, // mTime MStart MDuration
									1, // mCueID
									VideoMedia #3004 { // mMedia
										{ "/C:/Users/timsf/OneDrive/Documents/Watchout/Watchout 2017 MEDIA/NFL CFB MEDIA B" // mFile mPath
											"IN/N273_Comp_MatchupStadium-Environment_TOP_HAP.mov", 636997388, 1510489686, false, false, false, false }, // mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										true, // mStagePreview
										{ 1920, 1080 }, // mDim x y
										1, // mAlphaMode
										0, // mForcedAlphaMode
										false, // mSuppressThumbnail
										false, // mIsPreSplit
										false, // mIsStereoscopic
										false, // mIsImageSequence
										30.03, // mDuration
										false, // mUsePreviewMovie
										{ "", 0, 0, false, false, false, false }, // mPreviewMovie mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										"", // mMultiFileExt
										true, // mAllowHardwareAcc
										true, // mDoFrameBlend
										1, // mFrameRate
										"", // mIsBaseName
										0, // mIsFirstSeqNumber
										1, // mIsNumberOfFiles
										1, // mIsNumberOfDigits
										0, // mAudioNumOutput
										"", // mIsExtension
										0 // mDdsFlavour
									},
									0.0, // mPreroll
									{ // mParams
										AnchorTweenPointQuad {
											0, // mTimePos
											false, // mSmooth
											{ 960, 540, 0 } // mValue x y z
										}
									},
									0, // mPreviewQuality
									{ 5660, 1940, 0 }, // mInitialPos x y z
									false, // mOrientAlongPath
									false, // mRenderAsMaskOnly
									0, // mMask
									0, // mBlend
									false, // mExplicitTarget
									#0, // mPlayThroughDisplay
									#0, // mShader
									0, // mStacking
									0, // mOrientation
									false, // mLocalVanishingPoint
									"", // mInteractive
									false, // mExtTransform
									0.0, // mInTime
									false, // mLooping
									false, // mFreeRunning
									100, // mTimeScalePercentage
									1, // mExpectedAlphaMode
									{ // mOutputAssignments
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0
									},
									{ // mChannelMapping
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1
									}
								},
								ContMediaCue {
									{ 32.03, 30.03 }, // mTime MStart MDuration
									2, // mCueID
									VideoMedia #3005 { // mMedia
										{ "/C:/Users/timsf/OneDrive/Documents/Watchout/Watchout 2017 MEDIA/NFL CFB MEDIA B" // mFile mPath
											"IN/N274_Comp_MatchupStadium-Environment_BOTTOM_HAP.mov", 765425237, 1510489592, false, false, false, false }, // mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										true, // mStagePreview
										{ 1920, 1080 }, // mDim x y
										1, // mAlphaMode
										0, // mForcedAlphaMode
										false, // mSuppressThumbnail
										false, // mIsPreSplit
										false, // mIsStereoscopic
										false, // mIsImageSequence
										30.03, // mDuration
										false, // mUsePreviewMovie
										{ "", 0, 0, false, false, false, false }, // mPreviewMovie mPath mFileSize mModDate mHasURL mIsProxy mNoDownload mAutoRefresh
										"", // mMultiFileExt
										true, // mAllowHardwareAcc
										true, // mDoFrameBlend
										1, // mFrameRate
										"", // mIsBaseName
										0, // mIsFirstSeqNumber
										1, // mIsNumberOfFiles
										1, // mIsNumberOfDigits
										0, // mAudioNumOutput
										"", // mIsExtension
										0 // mDdsFlavour
									},
									0.0, // mPreroll
									{ // mParams
										AnchorTweenPointQuad {
											0, // mTimePos
											false, // mSmooth
											{ 960, 540, 0 } // mValue x y z
										}
									},
									0, // mPreviewQuality
									{ 5660, 1940, 0 }, // mInitialPos x y z
									false, // mOrientAlongPath
									false, // mRenderAsMaskOnly
									0, // mMask
									0, // mBlend
									false, // mExplicitTarget
									#0, // mPlayThroughDisplay
									#0, // mShader
									0, // mStacking
									0, // mOrientation
									false, // mLocalVanishingPoint
									"", // mInteractive
									false, // mExtTransform
									0.0, // mInTime
									false, // mLooping
									false, // mFreeRunning
									100, // mTimeScalePercentage
									1, // mExpectedAlphaMode
									{ // mOutputAssignments
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0
									},
									{ // mChannelMapping
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										0,
										1
									}
								}
							},
							false, // mExpanded
							2, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						},
						{
							"", // mName
							{ // mCues
							},
							false, // mExpanded
							3, // mIndex
							0, // mConditional
							false, // mDisabled
							0, // mStandBy
							false, // mLocked
							false, // mSpecLevels
							0 // mLevels
						}
					},
					2, // mCurrLayerIndex
					200, // mTimeScale
					10:00.0, // mDuration
					2, // mCueIDSeed
					true, // mFrontmostAtTop
					{ 0, 0, 0, 0, 0, false, 0, 0, 0 }, // MWinState mState mLeft mTop mWidth mHeight mActive MSashPos MHdrWidth MVScrollPos
					false, // mFixedDuration
					false, // mSpecTiers
					0, // mTiers
					0 // mAlwaysOnTop
				}
			}
		},
		"TaskListItem" // mClassName
	}
}
'''
testText = testText.splitlines()
filename = 'BTM-HOLIDAY_SKYLINE_02_1223.mp4'

fileScanner = scanner(filename,testText)